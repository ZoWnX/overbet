from django.db import models

from pytz import common_timezones

from users.models import User

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=256)
    timezone = models.CharField(
        max_length=256,
        choices=[(item,item) for item in common_timezones],
        default='UTC',
    )
    public = models.BooleanField(default=False)
    created_by = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name