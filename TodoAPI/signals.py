from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.models import User

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        print('Profile Created')

@receiver(post_save,sender=User)
def update_profile(sender,instance,created,**kwargs):
    if not created:
        instance.Profile.save()
        print('Profile Updated')

