from django.conf import settings
from django.db import models


class Playlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="playlists")
    title = models.CharField(max_length=180)
    description = models.TextField(blank=True)
    is_private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class PlaylistItem(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name="items")
    video = models.ForeignKey("videos.Video", on_delete=models.CASCADE, related_name="playlist_items")
    position = models.PositiveIntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["playlist", "video"], name="unique_playlist_item")]

    def __str__(self):
        return f"{self.playlist.title} - {self.video.title}"
