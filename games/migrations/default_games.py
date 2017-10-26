# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

def load_default_game_data(apps, schema_editor):
  # We get the model from the versioned app registry;
  # if we directly import it, it'll be the wrong version
	Game = apps.get_model("games", "Game")
	User = apps.get_model('users', 'User')
	Variant = apps.get_model('games', 'Variant')
	Currency = apps.get_model('currencies', 'Currency')
	u = User.objects.get(email='joshuawjulian@gmail.com')
	holdem = Variant.objects.get(title='No Limit Texas Hold\'em')
	plo = Variant.objects.get(title='Pot Limit Omaha')
	dollar = Currency.objects.get(code='USD')
	db_alias = schema_editor.connection.alias
	Game.objects.using(db_alias).bulk_create([
    Game(variant=holdem, blind_structure="$1/$2", currency=dollar,
				 min_buyin="$40", max_buyin="$200", public=True, created_by=u),
		Game(variant=holdem, blind_structure="$2/$5", currency=dollar,
				 min_buyin="$100", max_buyin="$500", public=True, created_by=u),
  	Game(variant=holdem, blind_structure="$5/$10", currency=dollar,
				 min_buyin="$500", max_buyin="$2000", public=True, created_by=u),
  
  ])

def unload_default_game_data(apps, schema_editor):
	# We get the model from the versioned app registry;
  # if we directly import it, it'll be the wrong version
  Game = apps.get_model("games", "Game")
  db_alias = schema_editor.connection.alias
  Game.objects.all().delete()

class Migration(migrations.Migration):

  dependencies = [
		('users', 'create_default_users'),
    ('games', '0001_initial'),
		('games', 'default_variants'),
		('currencies', 'load_currencies'),
  ]
    
  operations = [
    migrations.RunPython(load_default_game_data,unload_default_game_data),
  ]