from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("channels", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=50, unique=True)),
                ("slug", models.SlugField(max_length=60, unique=True)),
            ],
            options={"ordering": ["name"]},
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Video",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200)),
                ("slug", models.SlugField(max_length=230, unique=True)),
                ("description", models.TextField(blank=True)),
                ("thumbnail", models.ImageField(blank=True, null=True, upload_to="videos/thumbnails/")),
                ("video_file", models.FileField(blank=True, null=True, upload_to="videos/uploads/")),
                ("duration", models.PositiveIntegerField(default=0)),
                ("visibility", models.CharField(choices=[("public", "Public"), ("unlisted", "Unlisted"), ("private", "Private")], default="public", max_length=20)),
                ("status", models.CharField(choices=[("uploading", "Uploading"), ("processing", "Processing"), ("ready", "Ready"), ("failed", "Failed")], default="uploading", max_length=20)),
                ("view_count", models.PositiveIntegerField(default=0)),
                ("like_count", models.PositiveIntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("category", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="videos.category")),
                ("channel", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="videos", to="channels.channel")),
            ],
            options={"ordering": ["-created_at"], "indexes": [models.Index(fields=["status", "visibility", "created_at"], name="videos_video_status_9f8d29_idx"), models.Index(fields=["category", "created_at"], name="videos_video_category_8e4a49_idx"), models.Index(fields=["title"], name="videos_video_title_5e1fe4_idx")]},
        ),
        migrations.CreateModel(
            name="VideoLike",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("video", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="likes", to="videos.video")),
            ],
        ),
        migrations.CreateModel(
            name="VideoReport",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("reason", models.CharField(choices=[("spam", "Spam"), ("copyright", "Copyright"), ("misleading", "Misleading content"), ("abusive", "Abusive language"), ("other", "Other")], max_length=30)),
                ("note", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("video", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="reports", to="videos.video")),
            ],
        ),
        migrations.CreateModel(
            name="WatchHistory",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("watched_at", models.DateTimeField(auto_now_add=True)),
                ("progress_seconds", models.PositiveIntegerField(default=0)),
                ("video", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="watch_history", to="videos.video")),
            ],
        ),
    ]
