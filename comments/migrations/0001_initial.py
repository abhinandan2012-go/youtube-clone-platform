from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("videos", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="VideoComment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("body", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("parent", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name="replies", to="comments.videocomment")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="comments", to="accounts.user")),
                ("video", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="comments", to="videos.video")),
            ],
            options={"ordering": ["created_at"]},
        ),
    ]
