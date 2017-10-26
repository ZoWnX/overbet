# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

def load_default_variant_data(apps, schema_editor):
  # We get the model from the versioned app registry;
  # if we directly import it, it'll be the wrong version
	Variant = apps.get_model("games", "Variant")
	User = apps.get_model('users', 'User')
	u = User.objects.get(email='joshuawjulian@gmail.com')
	db_alias = schema_editor.connection.alias
	Variant.objects.using(db_alias).bulk_create([
    Variant(title='No Limit Texas Hold\'em', public=True, created_by=u),
    Variant(title='Limit Texas Hold\'em', public=True, created_by=u),
    Variant(title='Pot Limit Omaha', public=True, created_by=u),
		Variant(title='Limit Omaha 8 or better', public=True, created_by=u),
		Variant(title='Pot Limit Omaha 8 or better', public=True, created_by=u),
		Variant(title='7 Card Stud', public=True, created_by=u),
])

def unload_default_variant_data(apps, schema_editor):
	# We get the model from the versioned app registry;
  # if we directly import it, it'll be the wrong version
  Variant = apps.get_model("games", "Variant")
  db_alias = schema_editor.connection.alias
  Variant.objects.all().delete()

class Migration(migrations.Migration):

  dependencies = [
		('users', 'create_default_users'),
    ('games', '0001_initial'),
  ]
    
  operations = [
    migrations.RunPython(load_default_variant_data,unload_default_variant_data),
  ]