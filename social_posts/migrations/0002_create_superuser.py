from django.db import migrations
import os


def create_superuser(apps, schema_editor):
    User = apps.get_model("auth", "User")

    username = os.environ.get("SUPERUSER_NAME")
    email = os.environ.get("SUPERUSER_EMAIL")
    password = os.environ.get("SUPERUSER_PASSWORD")

    if username and password:
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password,
            )


class Migration(migrations.Migration):

    dependencies = [
        ("social_posts", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
