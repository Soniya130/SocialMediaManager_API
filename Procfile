web: gunicorn socialmanager.wsgi
release: python manage.py migrate && python manage.py collectstatic --noinput
web: gunicorn SocialMediaManager.wsgi --bind 0.0.0.0:$PORT


