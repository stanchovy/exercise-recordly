from rest_framework import serializers
from recordly.models import Artist
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
