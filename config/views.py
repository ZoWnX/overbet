from django.views.generic import View
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages

# Create your views here.
def index(request):
  
  messages.debug(request, 'Debug Message Test.')
  messages.info(request, 'Info Message Test.')
  messages.success(request, 'Success Message Test.')
  messages.warning(request, 'Warning Message Test.')
  messages.error(request, 'Error Message Test.')
  
  return render(request, 'index/index.html',)