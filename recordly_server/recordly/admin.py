from django.contrib import admin
from recordly.models import Artist, Album, Song

# Register your models here.
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Song)
