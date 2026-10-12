from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST

from comments.forms import CommentForm
from comments.models import VideoComment
from videos.models import Video


@require_POST
@login_required
def add_comment(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.video = video
        comment.user = request.user
        comment.save()
    return redirect("video_detail", slug=video.slug)


@require_POST
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(VideoComment, id=comment_id, user=request.user)
    video = comment.video
    comment.delete()
    return redirect("video_detail", slug=video.slug)
