from django.db import models
from django.conf import settings


class Channel(models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="channel")
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="channels/avatars/", blank=True, null=True)
    banner = models.ImageField(upload_to="channels/banners/", blank=True, null=True)
    subscriber_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="subscriptions")
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name="subscribers")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["user", "channel"], name="unique_channel_subscription")]

    def __str__(self):
        return f"{self.user.username} -> {self.channel.name}"
