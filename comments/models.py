from django.db import models


class VideoComment(models.Model):
    video = models.ForeignKey("videos.Video", on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name="replies")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.user.username}: {self.body[:40]}"
