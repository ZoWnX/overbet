from django.db import models

from users.models import User
from locations.models import Location
from games.models import Game

# Create your models here.
class PokerSession(models.Model):

  user = models.ForeignKey(User, null=False)
  location = models.ForeignKey(Location, null=False)
  game = models.ForeignKey(Game, null=False)

  is_cash = models.BooleanField(default=True, null=False)
  public = models.BooleanField(default=True, null=False)
  active = models.BooleanField(default=True, null=False)

  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)
  deleted = models.BooleanField(default=False)

  @staticmethod
  def user_has_active_session(user):
    try:
      return PokerSession.objects.filter(user=user).get(active=True)
    except PokerSession.DoesNotExist:
      return False

  def session_updates(self):
    sessions = PokerSessionUpdate.objects.filter(poker_session=self).order_by('time')
    return sessions

  def latest_chip_stack(self):
    return self.all_chip_stacks().latest('time').chip_stack

  def latest_buy_in(self):
    return self.all_buy_ins().latest('time').buy_in

  def start_time(self):
    try:
      start_time = self.session_updates()[0].time
    except IndexError:
      start_time = None
    return start_time

  def latest_time(self):
    try:
      latest_time = self.session_updates().latest('time').time
    except IndexError:
      latest_time = None
    return latest_time

  def total_mins_played(self):
    return self.latest_time() - self.start_time()

  def all_buy_ins(self):
    return self.session_updates().exclude(buy_in__isnull=True)

  def all_chip_stacks(self):
    return self.session_updates().exclude(chip_stack__isnull=True)

  def net(self):
    return self.latest_chip_stack() - self.latest_buy_in()


class PokerSessionUpdate(models.Model):
  poker_session = models.ForeignKey(PokerSession)
  time = models.DateTimeField(null=False, blank=False)

  buy_in = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
  chip_stack = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)

class PokerSessionComment(models.Model):
  user = models.ForeignKey(User)
  poker_session = models.ForeignKey(PokerSession, null=False, blank=False, default=0)
  time = models.DateTimeField(null=False, blank=False)
  text = models.TextField()
  created_on = models.DateTimeField(auto_now_add=True)

  deleted = models.BooleanField(default=False)
