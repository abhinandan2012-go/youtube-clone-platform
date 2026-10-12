from django.conf import settings
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=60, unique=True)

    class Meta:
        ordering = ["name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Video(models.Model):
    STATUS_CHOICES = [
        ("uploading", "Uploading"),
        ("processing", "Processing"),
        ("ready", "Ready"),
        ("failed", "Failed"),
    ]
    VISIBILITY_CHOICES = [
        ("public", "Public"),
        ("unlisted", "Unlisted"),
        ("private", "Private"),
    ]

    channel = models.ForeignKey("channels.Channel", on_delete=models.CASCADE, related_name="videos")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="videos")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=230, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    thumbnail = models.ImageField(upload_to="videos/thumbnails/", blank=True, null=True)
    video_file = models.FileField(upload_to="videos/uploads/", blank=True, null=True)
    duration = models.PositiveIntegerField(default=0)
    visibility = models.CharField(max_length=20, choices=VISIBILITY_CHOICES, default="public")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="uploading")
    view_count = models.PositiveIntegerField(default=0)
    like_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["status", "visibility", "created_at"]),
            models.Index(fields=["category", "created_at"]),
            models.Index(fields=["title"]),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class VideoLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="video_likes")
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["user", "video"], name="unique_video_like")]

    def __str__(self):
        return f"{self.user.username} likes {self.video.title}"


class VideoReport(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="reports")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="video_reports")
    reason = models.CharField(max_length=30, choices=[
        ("spam", "Spam"),
        ("copyright", "Copyright"),
        ("misleading", "Misleading content"),
        ("abusive", "Abusive language"),
        ("other", "Other"),
    ])
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} reported {self.video.title}"


class WatchHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="watch_history")
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="watch_history")
    watched_at = models.DateTimeField(auto_now_add=True)
    progress_seconds = models.PositiveIntegerField(default=0)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["user", "video"], name="unique_watch_history")]

    def __str__(self):
        return f"{self.user.username} watched {self.video.title}"
