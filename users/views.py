from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.conf import settings

from . import forms
from .models import User, UserProfile

def profile_view(request, email=None):
  context = {}
  if request.method == 'GET':
    if id is None:
      if request.user.is_authenticated():
        return redirect('users:profile_view', email=request.user.email)
      else:
        messages.error(request, 'User must be logged in to view own profile')
        return redirect('users:login')
    else:
      user = User.objects.get(email=email)
      if user is not None:
        profile = UserProfile.objects.get(user=user)
        context['profile'] = profile
      else:
        messages.error(request, 'ID does not exist')
        return redirect('users:login')
  return render(request, 'users/profile_view.html', context)

def logout(request):
  auth_logout(request)
  messages.success(request, 'User has been successfully logged out')
  return redirect('users:login')

def register(request):
  context = {}
  if request.method == 'POST':
    form = forms.RegisterForm(request.POST)
    if form.is_valid():
      cleaned = form.cleaned_data
      if cleaned['password'] != cleaned['password_again']:
        messages.error(request, 'Passwords do not match')
      else:
        try:
          User.objects.create_user(cleaned['email'], cleaned['password'])
          messages.success(request, 'User {0} created'.format(cleaned['email']))
          return redirect('users:login')
        except IntegrityError:
          messages.error(request, 'Email address already used')
  else:
    form = forms.RegisterForm()

  context['form'] = form
  return render(request, 'users/register.html', context)

def login(request):
  context = {}
  if request.method == 'POST':
    form = forms.LoginForm(request.POST)
    if form.is_valid():
      email = form.cleaned_data['email']
      password = form.cleaned_data['password']
      user = authenticate(email=email, password=password)
      if user is not None:
        auth_login(request, user)
        messages.success(request, '{0} successfully logged in'.format(email))
        return redirect('index')
      else:
        messages.error(request, 'Bad email/password combination')
  else:
      form = forms.LoginForm()

  context['form'] = form
  return render(request, 'users/login.html', context)