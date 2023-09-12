import lyricsgenius

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .modules.geniuscards import createImage
from .forms import MainForm

global genius
genius = lyricsgenius.Genius("")


def index(request):

    template = loader.get_template("geniuscards/index.html")

    form = MainForm(request.POST)
    if request.method == "POST":
        encoded_image = ""
        if form.is_valid():
            song_title = form.cleaned_data["song_title"]
            song_author = form.cleaned_data["song_author"]
            song_lyrics = form.cleaned_data["song_lyrics"]
            song_image_name = form.cleaned_data["song_image"]
            song_image_base64 = form.cleaned_data["song_image_base64"]
            encoded_image = createImage(song_image_base64, song_lyrics,
                song_author, song_title)
            encoded_image = "data:image/png;base64,"+encoded_image
        else:
            form = MainForm()
        context = {
            'encoded_image': encoded_image,
            'form': form
        }
    else:
        form = MainForm()
        context = {'form': form}
    return HttpResponse(template.render(context, request))


@csrf_exempt
def get_song_data(request):
    author = request.POST.dict().get("author")
    song = request.POST.dict().get("song")
    artist = genius.search_artist(author, max_songs=0)
    songs = genius.search_song(song, artist.name)
    print(songs)
    return JsonResponse({"song": songs.lyrics})
