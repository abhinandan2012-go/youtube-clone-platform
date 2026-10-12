from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from channels.models import Channel, Subscription


def channel_detail(request, slug):
    channel = get_object_or_404(Channel, slug=slug)
    videos = channel.videos.filter(visibility="public")
    return render(request, "channels/detail.html", {"channel": channel, "videos": videos})


@login_required
def channel_dashboard(request):
    channel = request.user.channel
    return render(request, "channels/dashboard.html", {"channel": channel})


@login_required
def toggle_subscription(request, slug):
    channel = get_object_or_404(Channel, slug=slug)
    if request.user == channel.owner:
        return redirect("channel_detail", slug=channel.slug)

    subscription, created = Subscription.objects.get_or_create(user=request.user, channel=channel)
    if not created:
        subscription.delete()
    return redirect("channel_detail", slug=channel.slug)
