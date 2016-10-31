from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model):
    name = models.CharField(max_length=100)
    is_favorite = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('name', 'user')

class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist)
    is_favorite = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('title', 'artist', 'user')

class Song(models.Model):
    title = models.CharField(max_length=200)
    album = models.ForeignKey(Album, related_name='songs')
    is_favorite = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('title', 'album', 'user')