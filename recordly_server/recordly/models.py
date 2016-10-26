from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model):
    name = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Album(models.Model):
    title = models.CharField(max_length=200, unique=True)
    artist = models.ForeignKey(Artist)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Song(models.Model):
    title = models.CharField(max_length=200, unique=True)
    album = models.ForeignKey(Album)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
