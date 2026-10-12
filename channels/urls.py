from django.urls import path

from . import views

urlpatterns = [
    path("<slug:slug>/", views.channel_detail, name="channel_detail"),
    path("<slug:slug>/subscribe/", views.toggle_subscription, name="toggle_subscription"),
    path("dashboard/", views.channel_dashboard, name="channel_dashboard"),
]
