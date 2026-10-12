from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from channels.models import Channel

from .forms import LoginForm, ProfileForm, SignupForm


def signup_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            Channel.objects.get_or_create(
                owner=user,
                defaults={
                    "name": user.username,
                    "slug": user.username.lower().replace(" ", "-"),
                    "description": "New creator on Videoflow.",
                },
            )
            user = authenticate(username=user.username, password=form.cleaned_data["password1"])
            if user is not None:
                login(request, user)
                messages.success(request, "Your account was created successfully.")
                return redirect("home")
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})


@login_required
def profile_view(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated.")
            return redirect("profile")
    else:
        form = ProfileForm(instance=request.user)
    return render(request, "accounts/profile.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")
