from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError, transaction
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django import utils
from django.forms.formsets import formset_factory

from datetime import datetime, timedelta
from pytz import timezone
import pytz



from locations.models import Location
from games.models import Game
from .models import PokerSession, PokerSessionUpdate
from .forms import StartPokerSessionForm, PokerSessionUpdateForm, PokerSessionUpdateEditForm, PokerSessionForm

@login_required
def edit(request, id):
  context = {}
  user = request.user

  # Create the formset, specifying the form and formset we want to use.
  UpdateFormSet = formset_factory(PokerSessionUpdateEditForm)
  poker_session = PokerSession.objects.get(pk=id)
  tz = timezone(poker_session.location.timezone)
  
  if(request.method == "POST"):
    print("Method is post")
    poker_session_form = PokerSessionForm(request.POST)
    update_formset = UpdateFormSet(request.POST)

    if(poker_session_form.is_valid() and update_formset.is_valid()):
      print ("Both forms valid")
      poker_session.location = poker_session_form.cleaned_data['location']
      poker_session.game = poker_session_form.cleaned_data['game']
      poker_session.public = poker_session_form.cleaned_data['public']
      poker_session.is_cash = poker_session_form.cleaned_data['is_cash']

      poker_session.save()

      new_updates = []

      for update_form in update_formset:
        clean = update_form.cleaned_data
        time = clean.get('time')
        if time is None:
          continue

        time = tz.localize(time.replace(tzinfo=None)).astimezone(pytz.utc)

        chip_stack = clean['chip_stack']
        buy_in = clean['buy_in']
        comment = clean['comment']
        if not (chip_stack is None and buy_in is None and comment is None):
          new_updates.append(PokerSessionUpdate(
            poker_session=poker_session,
            time=time,
            chip_stack=chip_stack,
            buy_in=buy_in,
            comment=comment
          ))

      #ATOMICALLY - Delete all the old Updates, then jam in all the new updates
      try:
        with transaction.atomic():
          PokerSessionUpdate.objects.filter(poker_session=poker_session).delete()
          PokerSessionUpdate.objects.bulk_create(new_updates)
          messages.success(request, 'Poker Session Updated')
      except IntegrityError:
        messages.error(request, "There was an error with the update")
    else: #forms not valid
      context = {
        'poker_session_form': poker_session_form,
        'update_formset': update_formset,
        'poker_session': poker_session,
      }
      return render(request, 'pokersessions/edit.html', context)

  updates = poker_session.session_updates()
  update_info = []
  for update in updates:
      time = update.time.astimezone(tz)
      update_info.append({
          'time': time.strftime(settings.DATE_TIME_FORMAT_LONG),
          'buy_in': update.buy_in,
          'chip_stack': update.chip_stack,
          'comment': update.comment
      })
  poker_session_form = PokerSessionForm(instance=poker_session)
  update_formset = UpdateFormSet(initial=update_info)

  context = {
      'poker_session_form': poker_session_form,
      'update_formset': update_formset,
      'poker_session': poker_session,
  }

  return render(request, 'pokersessions/edit.html', context)
  
  

@login_required
def list(request):
  context = {}
  
  sessions = PokerSession.objects.filter(user=request.user)
  context['sessions'] = sessions
    
  return render(request, 'pokersessions/list.html', context)

@login_required
def start(request):
  context = {}
  if request.method == 'GET':
    
    #check if the user has a session already started
    if PokerSession.user_has_active_session(request.user):
      messages.error(request, 'user has active session')
      return redirect("pokersessions:active")
    
    locations_public = Location.objects.filter(public=True).exclude(deleted=True)
    games_public = Game.objects.filter(public=True).exclude(deleted=True)
    
    locations_private = Location.objects.filter(created_by=request.user).exclude(deleted=True)
    games_private = Game.objects.filter(created_by=request.user).exclude(deleted=True)
    
    locations = locations_public | locations_private
    games = games_public | games_private
    
    form = StartPokerSessionForm()
    form.fields['location'].queryset = locations
    form.fields['game'].queryset = games
    
    context['form'] = form
    
    return render(request, 'pokersessions/start.html', context)
  else:
    form = StartPokerSessionForm(request.POST)
    if form.is_valid():
      cleaned = form.cleaned_data
      ps = PokerSession(user=request.user,
                        location=cleaned['location'],
                        game=cleaned['game'],
                        is_cash=cleaned['is_cash'],
                        active=True)
      ps.save()
      psu = PokerSessionUpdate(poker_session=ps,
                               time=utils.timezone.now(),
                               comment='Session Start',
                               buy_in=cleaned['buy_in'],
                               chip_stack=cleaned['buy_in'])
      psu.save()
      return redirect('pokersessions:active')
    else:
      context['form'] = form
      return render(request, 'pokersessions/start.html', context)

@login_required
def active(request):
  context = {}
  if not PokerSession.user_has_active_session(request.user):
    messages.error(request, 'user does not have active session')
    return redirect("pokersessions:start")
  
  active_session = PokerSession.user_has_active_session(request.user)
  context['active_session'] = active_session
  
  if request.method == 'POST':
    form = PokerSessionUpdateForm(request.POST)  
    if form.is_valid():
      cleaned = form.cleaned_data
      psu = PokerSessionUpdate(poker_session=active_session,
                               time=utils.timezone.now(),
                               comment=cleaned['comment'],
                               buy_in=cleaned['buy_in'],
                               chip_stack=cleaned['chip_stack'])
      psu.save()  
    if request.POST.get('end_update'):
      active_session.active = False
      active_session.save()
      messages.success(request, 'Poker Session Ended')
      return redirect("pokersessions:start")
    
  form = PokerSessionUpdateForm()
  context['form'] = form
  return render(request, 'pokersessions/active.html', context)
    