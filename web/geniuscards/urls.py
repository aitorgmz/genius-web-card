from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("getSongData", views.get_song_data, name="get_song_data"),
]