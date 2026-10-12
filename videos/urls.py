from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("search/", views.search_view, name="search"),
    path("upload/", views.upload_video_view, name="upload_video"),
    path("<slug:slug>/", views.video_detail_view, name="video_detail"),
]
