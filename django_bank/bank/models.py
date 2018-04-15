from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver


from time import time

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=10000)
    transaction_password = models.CharField(max_length = 30)
    account_no = models.IntegerField(unique=True,default=1000)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Transaction(models.Model):
    receiver_accno = models.IntegerField()
    sender_accno = models.IntegerField(default=1000)
    amount = models.IntegerField()
    transaction_password = models.CharField(max_length=30)
    #def __str__(self):
    #    return self.receiver_accno.account_no
