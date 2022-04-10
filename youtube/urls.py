from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('VideoDownloader', views.ytb_down, name='ytb_down'),
    path('MusicDownloader', views.music, name='msic'),
    path('ThumbnailDownloader', views.thumbnail, name='thumbnail'),

]