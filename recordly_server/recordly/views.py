import sys
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import login as django_login, authenticate, logout as django_logout
from django.shortcuts import render_to_response, redirect, render

from recordly.models import Artist, Album, Song
import recordly.serializers as serializers
from rest_framework import generics

# for API view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

class LoginView(APIView):
    def get(self, request, format=None):
        template = loader.get_template('login.html')
        context = {
        }
        return HttpResponse(template.render(context, request))

class RecordlyView(APIView):
    def get(self, request, format=None):
        template = loader.get_template('recordly.html')
        context = {
        }
        return HttpResponse(template.render(context, request))

class DoLogin(APIView):
    def get(self, request, format=None):
        return Response('post to this form to do login')
    def post(self, request, format=None):
        print >> sys.stderr, request.POST
        # user = authenticate(email=request.POST['username'], password=request.POST['password'])
        user = authenticate(email='usera', password='welcome1')
        if user is not None:
            if user.is_active:
                django_login(request, user)
                return redirect('/recordly')
            else:
                return redirect('/?error=auth&code=UserNotActive')
        else:
            return redirect('/?error=auth&code=InvalidPassword')

class Albums(generics.ListAPIView):
    serializer_class = serializers.AlbumSerializer
    lookup_url_kwarg = 'filter'
    def get_queryset(self):
        query_filter = self.kwargs.get(self.lookup_url_kwarg)
        if query_filter == 'favorites':
            return Album.objects.filter(user=self.request.user, is_favorite=True)
        else:
            return Album.objects.filter(user=self.request.user)

class Artists(generics.ListAPIView):
    serializer_class = serializers.ArtistSerializer
    lookup_url_kwarg = 'filter'
    def get_queryset(self):
        query_filter = self.kwargs.get(self.lookup_url_kwarg)
        if query_filter == 'favorites':
            return Artist.objects.filter(user=self.request.user, is_favorite=True)
        else:
            return Artist.objects.filter(user=self.request.user)

class Songs(generics.ListAPIView):
    serializer_class = serializers.SongSerializer
    lookup_url_kwarg = 'filter'
    def get_queryset(self):
        query_filter = self.kwargs.get(self.lookup_url_kwarg)
        if query_filter == 'favorites':
            return Song.objects.filter(user=self.request.user, is_favorite=True)
        else:
            return Song.objects.filter(user=self.request.user)

class Search(APIView):
    def get(self, request, searchterm, format=None):
        songs = Song.objects.filter(user=self.request.user, title__contains=searchterm)
        serializer = serializers.SongSerializer(songs, many=True)
        return Response(serializer.data)
