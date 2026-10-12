from django.urls import path

from . import views

urlpatterns = [
    path("", views.playlist_list, name="playlist_list"),
    path("create/", views.create_playlist, name="create_playlist"),
    path("<int:playlist_id>/", views.playlist_detail, name="playlist_detail"),
    path("add/<int:video_id>/", views.add_to_playlist, name="add_to_playlist"),
]
