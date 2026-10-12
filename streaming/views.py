from django.http import HttpResponse
from django.shortcuts import render


def stream_home(request):
    return HttpResponse("Streaming service ready.")


def hls_manifest(request, video_id):
    return render(request, "streaming/manifest.m3u8", {"video_id": video_id}, content_type="application/vnd.apple.mpegurl")
