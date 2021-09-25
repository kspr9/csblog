from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# This file enables the creation of profile while User is created, other part in app.py

# when user is saved, send 'post_save' signal which is being received by receiver ie create_profile func
# create_profile takes all the arguments passed by post_save; instance marks the user and created=true/false
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # if instance of User is created create profile object with user = instance of the User that was created
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
