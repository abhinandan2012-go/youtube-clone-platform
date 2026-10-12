from django import forms

from videos.models import Video


class VideoUploadForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Comma-separated tags")

    class Meta:
        model = Video
        fields = ["title", "description", "category", "thumbnail", "visibility", "video_file", "tags"]

    def clean_video_file(self):
        file = self.cleaned_data.get("video_file")
        if file:
            ext = file.name.split(".")[-1].lower()
            allowed = {"mp4", "mov", "webm", "mkv"}
            if ext not in allowed:
                raise forms.ValidationError("Unsupported video format. Use MP4, MOV, WEBM, or MKV.")
            if file.size > 500 * 1024 * 1024:
                raise forms.ValidationError("Video file exceeds 500MB upload limit.")
        return file
