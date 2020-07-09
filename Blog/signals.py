from django.db.models.signals import post_save
from django.contrib.auth.models import User
from notifications.signals import notify
from django.dispatch import receiver
from .models import Like


def my_handler(sender, instance, created, **kwargs):
    notify.send(instance, "was created")


post_save.connect(my_handler, sender=Like)