from django import forms

from comments.models import VideoComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = VideoComment
        fields = ["body"]
        widgets = {"body": forms.Textarea(attrs={"rows": 3, "placeholder": "Share your thoughts..."})}
