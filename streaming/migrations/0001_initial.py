from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("videos", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="HlsStream",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("manifest_url", models.URLField(blank=True, null=True)),
                ("status", models.CharField(default="queued", max_length=20)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("video", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="stream_jobs", to="videos.video")),
            ],
        ),
    ]
