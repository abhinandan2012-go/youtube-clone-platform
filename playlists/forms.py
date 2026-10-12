from django import forms

from playlists.models import Playlist


class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ["title", "description", "is_private"]
