import logging

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .modules.geniuscards import createImage
from .forms import MainForm


def index(request):

    template = loader.get_template("geniuscards/index.html")

    if request.method == "POST":
        form = MainForm(request.POST)
        if form.is_valid():
            song_title = form.cleaned_data["song_title"]
            song_author = form.cleaned_data["song_author"]
            song_lyrics = form.cleaned_data["song_lyrics"]
            song_image_name = form.cleaned_data["song_image"]
            song_image_base64 = form.cleaned_data["song_image_base64"]
            print("Value: ", song_image_base64)
            encoded_image = createImage(song_image_base64, song_lyrics,
                song_author, song_title)
            encoded_image = "data:image/png;base64,"+encoded_image
            context = {
                'encoded_image': encoded_image,
                'form': form
            }
    else:
        form = MainForm()
        context = {'form': form}
    return HttpResponse(template.render(context, request))
