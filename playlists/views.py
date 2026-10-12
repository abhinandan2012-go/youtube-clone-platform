from django.shortcuts import render


def playlist_list(request):
    return render(request, "playlists/list.html", {})


def create_playlist(request):
    return render(request, "playlists/create.html", {})


def playlist_detail(request, playlist_id):
    return render(request, "playlists/detail.html", {"playlist_id": playlist_id})


def add_to_playlist(request, video_id):
    return render(request, "playlists/add.html", {"video_id": video_id})
