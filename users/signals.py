from .models import UserProfile, User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
  print("create_user_profile")
  if created:
    UserProfile.objects.create(user=instance)