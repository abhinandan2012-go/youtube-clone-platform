from django.conf import settings
from django.db import models


class HlsStream(models.Model):
    video = models.ForeignKey("videos.Video", on_delete=models.CASCADE, related_name="stream_jobs")
    manifest_url = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=20, default="queued")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.video.title} - {self.status}"
