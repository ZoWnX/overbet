from django import forms
from django.conf import settings

from .models import Location

class LocationForm(forms.ModelForm):
  class Meta:
    model = Location
    fields = ['name', 'timezone']
  