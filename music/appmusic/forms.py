from django import forms
from .models import Song

class CustomCreateSong(forms.ModelForm):
    category = forms.ChoiceField(choices=Song.CATEGORY_CHOICES, widget=forms.Select)
    image = forms.ImageField(required=True)
    audio_file = forms.FileField(required=True)

    class Meta:
        model = Song
        fields = ('title', 'artist', 'category', 'image' ,'audio_file')