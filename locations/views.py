from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required

from datetime import datetime, timedelta
from pytz import timezone
import pytz

from .models import Location
from .forms import LocationForm

@login_required
def list(request):
  context = {}
  if request.method == 'GET':
    locations = Location.objects.filter(public=True) | Location.objects.filter(created_by=request.user)
    context['locations'] = locations
    
  return render(request, 'locations/list.html', context)

def add(request):
  context = {}
  
  if request.method == 'POST':
    form = LocationForm(request.POST)
    if form.is_valid():
      location = Location()
      location.name = form.cleaned_data['name']
      location.timezone = form.cleaned_data['timezone']
      location.public = False
      location.created_by = request.user
      location.save()
      messages.success(request, "%s was created!" % (location.name))
      return redirect('locations:list')
  elif request.method == 'GET':
    form = LocationForm()
    context['form'] = form
    
  return render(request, 'locations/add.html', context)

@login_required
def edit(request, id):
  context = {}
  location = Location.objects.get(id=id)
  
  if location == None:
    messages.error(request, "Location does not exist")
    return redirect('locations:list')
  
  if request.method == 'POST':
    form = LocationForm(request.POST)
    if form.is_valid():
      location.name = form.cleaned_data['name']
      location.timezone = form.cleaned_data['timezone']
      location.save()
      messages.success(request, "%s was updated!" % (location.name))
      return redirect('locations:list')
  elif request.method == 'GET':
    form = LocationForm(instance=location)
    context['form'] = form
    context['id'] = id
    
  return render(request, 'locations/edit.html', context)