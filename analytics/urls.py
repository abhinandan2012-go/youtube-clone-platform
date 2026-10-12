from django.urls import path

from . import views

urlpatterns = [
    path("dashboard/", views.creator_dashboard, name="creator_dashboard"),
]
