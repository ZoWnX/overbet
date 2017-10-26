from django.db import models

from users.models import User
from currencies.models import Currency
from locations.models import Location

class Game(models.Model):
  variant = models.ForeignKey("Variant")
  blind_structure = models.CharField(max_length=256)
  currency = models.ForeignKey(Currency)
  min_buyin = models.CharField(max_length=256)
  max_buyin = models.CharField(max_length=256)
  comments = models.TextField(null=True)
  
  locations = models.ManyToManyField(Location)
  
  public = models.BooleanField(default=False)
  created_by = models.ForeignKey(User)
  
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)
  deleted = models.BooleanField(default=False)
  
  def __str__(self):
    return self.short_name()
  
  def short_name(self):
    return "%s %s (%s - %s)" % (self.blind_structure, self.variant, self.min_buyin, self.max_buyin)
    
  
class Variant(models.Model):
  title = models.CharField(max_length=256)
  
  public = models.BooleanField(default=False)
  created_by = models.ForeignKey(User)
  
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)
  deleted = models.BooleanField(default=False)
  
  def __str__(self):
    return self.title