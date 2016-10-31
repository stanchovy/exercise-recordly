from rest_framework import serializers
from recordly.models import Artist, Album, Song
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song

class AlbumSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True)
    class Meta:
        model = Album
