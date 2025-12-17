from django.db import migrations

def create_superuser(apps, schema_editor):
    from django.contrib.auth.models import User
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='soniyapatil130',
            email='soniyaapatil30@gmail.com',
            password='Soniya@130'
        )

class Migration(migrations.Migration):

    dependencies = [
        ('social_posts', '0001_initial'),  # replace with your last migration
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
