# models.py

from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='following_from_profile')



