from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from channels.models import Channel
from comments.forms import CommentForm
from comments.models import VideoComment
from videos.forms import VideoUploadForm
from videos.models import Tag, Video, VideoLike


def home_view(request):
    videos = Video.objects.filter(visibility="public").select_related("channel", "owner", "category")[:12]
    return render(request, "videos/home.html", {"videos": videos})


def search_view(request):
    query = request.GET.get("q", "").strip()
    videos = Video.objects.filter(visibility="public")
    if query:
        videos = videos.filter(
            Q(title__icontains=query)
            | Q(description__icontains=query)
            | Q(owner__username__icontains=query)
            | Q(tags__name__icontains=query)
        ).distinct()
    return render(request, "videos/search_results.html", {"videos": videos, "query": query})


@login_required
def upload_video_view(request):
    if request.method == "POST":
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            channel, _ = Channel.objects.get_or_create(
                owner=request.user,
                defaults={
                    "name": request.user.username,
                    "slug": request.user.username.lower().replace(" ", "-"),
                },
            )
            video = form.save(commit=False)
            video.owner = request.user
            video.channel = channel
            video.status = "processing"
            video.save()

            tags_input = form.cleaned_data.get("tags", "")
            tag_names = [tag.strip() for tag in tags_input.split(",") if tag.strip()]
            for tag_name in tag_names:
                tag, _ = Tag.objects.get_or_create(name=tag_name)
                video.tags.add(tag)

            messages.success(request, "Your video is uploaded and queued for processing.")
            return redirect("video_detail", slug=video.slug)
    else:
        form = VideoUploadForm()
    return render(request, "videos/upload.html", {"form": form})


def video_detail_view(request, slug):
    video = get_object_or_404(Video, slug=slug, visibility="public")
    related_videos = Video.objects.filter(visibility="public").exclude(id=video.id).order_by("-created_at")[:6]
    comments = video.comments.select_related("user").all()
    like_count = video.likes.count()
    comment_form = CommentForm()

    if request.method == "POST" and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.video = video
            comment.user = request.user
            comment.save()
            return redirect("video_detail", slug=slug)
    return render(
        request,
        "videos/detail.html",
        {
            "video": video,
            "comments": comments,
            "related_videos": related_videos,
            "like_count": like_count,
            "comment_form": comment_form,
        },
    )


@require_POST
@login_required
def toggle_like(request, slug):
    video = get_object_or_404(Video, slug=slug)
    like, created = VideoLike.objects.get_or_create(user=request.user, video=video)
    if not created:
        like.delete()
    return redirect("video_detail", slug=slug)
