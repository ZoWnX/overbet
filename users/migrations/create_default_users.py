# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.auth.hashers import make_password

def load_users(apps, schema_editor):
  # We get the model from the versioned app registry;
  # if we directly import it, it'll be the wrong version
	User = apps.get_model('users', 'User')
	u = User()
	u.password = make_password('joshua')
	u.email = 'joshuawjulian@gmail.com'
	u.is_superuser = True
	u.is_staff = True
	u.save()

def unload_users(apps, schema_editor):
	# We get the model from the versioned app registry;
  # if we directly import it, it'll be the wrong version
  User = apps.get_model("users", "User")
  db_alias = schema_editor.connection.alias
  User.objects.all().delete()

class Migration(migrations.Migration):

  dependencies = [
    ('users', '0001_initial'),
  ]
    
  operations = [
    migrations.RunPython(load_users,unload_users),
  ]