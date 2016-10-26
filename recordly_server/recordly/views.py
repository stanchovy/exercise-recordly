from django.shortcuts import render

from recordly.models import Artist
import recordly.serializers as serializers
from rest_framework import generics

# for API view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


# Create your views here.
class Artists(generics.ListAPIView):
    serializer_class = serializers.ArtistSerializer
    def get_queryset(self):
        # return Artist.objects.filter(user=self.request.user)
        return Artist.objects.all()
