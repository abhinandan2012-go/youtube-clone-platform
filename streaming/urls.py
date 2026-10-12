from django.urls import path

from . import views

urlpatterns = [
    path("", views.stream_home, name="stream_home"),
    path("manifest/<int:video_id>/", views.hls_manifest, name="hls_manifest"),
]
