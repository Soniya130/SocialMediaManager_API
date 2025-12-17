from django.db import migrations
import os


def create_superuser(apps, schema_editor):
    from django.contrib.auth.models import User
    username = os.environ.get("SUPERUSER_NAME", "admin")
    email = os.environ.get("SUPERUSER_EMAIL", "soniyaapatil30@gmail.com")
    password = os.environ.get("SUPERUSER_PASSWORD", "admin12345")

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)


class Migration(migrations.Migration):
    dependencies = [
        ('social_posts', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(create_superuser),
    ]
