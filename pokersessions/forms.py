from django import forms
from django.conf import settings

from locations.models import Location
from games.models import Game
from .models import PokerSession, PokerSessionUpdate

class StartPokerSessionForm(forms.Form):
	location = forms.ModelChoiceField(
  	queryset=Location.objects.all(),
    empty_label=None,
    required=True,
    label="Location"
	)
	game = forms.ModelChoiceField(
  	queryset=Game.objects.all(),
    empty_label=None,
    required=True,
    label="Game"
  )
	buy_in = forms.DecimalField(
  	max_digits=15,
    decimal_places=2,
    required=True,
    label="Buy in"
  )
	is_cash = forms.BooleanField(label='Cash Game')

class PokerSessionUpdateForm(forms.Form):
	buy_in = forms.DecimalField(
  	max_digits=15,
    decimal_places=2,
    required=False,
    label="Buy in"
	)
	chip_stack = forms.DecimalField(
  	max_digits=15,
    decimal_places=2,
    required=False,
    label="Chip Stack"
  )

class PokerSessionUpdateEditForm(forms.ModelForm):
	class Meta:
		model= PokerSessionUpdate
		fields = {"time", 'buy_in', "chip_stack"}

class PokerSessionForm(forms.ModelForm):
	class Meta:
		model = PokerSession
		fields = {"location", "game", "is_cash", 'public', "active"}
