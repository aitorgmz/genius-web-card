import lyricsgenius

from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from decouple import config
from .modules.geniuscards import createImage
from .forms import MainForm

global genius
access_token = config('GENIUS_ACCESS_TOKEN')
genius = lyricsgenius.Genius(access_token)


def index(request):
    template = loader.get_template("geniuscards/index.html")
    form = MainForm()
    context = {'form': form}
    return HttpResponse(template.render(context, request))


@csrf_exempt
def get_song_data(request):
    author = request.POST.dict().get("author")
    song = request.POST.dict().get("song")
    artist = genius.search_artist(author, max_songs=0)
    songs = genius.search_song(song, artist.name)
    return JsonResponse({"songName": songs.title, "songAuthor": songs.artist, "song": str(songs.lyrics), "coverUrl": songs.song_art_image_url})


@csrf_exempt
def get_image_from_song_data(request):
    song = request.POST.dict().get("song")
    author = request.POST.dict().get("author")
    lyrics = request.POST.dict().get("lyrics")
    image_base64 = request.POST.dict().get("image")
    encoded_image = createImage(image_base64, lyrics,
                            author, song, False)
    return JsonResponse({"encodedImage": encoded_image})


@csrf_exempt
def get_image_from_local_data(request):
    song_title = request.POST.dict().get("song_title")
    song_author = request.POST.dict().get("song_author")
    song_lyrics = request.POST.dict().get("song_lyrics")
    song_image_base64 = request.POST.dict().get("song_image_base64")
    encoded_image = createImage(song_image_base64, song_lyrics,
                                song_author, song_title, True)
    encoded_image = "data:image/png;base64," + encoded_image
    return JsonResponse({encoded_image:encoded_image})