from django import forms


class MainForm(forms.Form):
    song_title = forms.CharField(label="Song Title", max_length=100)
    song_author = forms.CharField(label="Author", max_length=100)
    song_lyrics = forms.CharField(label="Lyrics", max_length=500, widget=forms.Textarea)
    song_image = forms.ImageField(label="Image", required=False)
    song_image_base64 = forms.CharField(widget=forms.HiddenInput(), initial=" ", required=False)
