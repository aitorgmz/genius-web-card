from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("getSongData", views.get_song_data, name="get_song_data"),
    path("getImageFromSongData", views.get_image_from_song_data, name="get_image_from_song_data"),
]