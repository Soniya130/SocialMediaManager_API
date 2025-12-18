release: python manage.py collectstatic --noinput
web: gunicorn socialmanager.wsgi --log-file -
web: python manage.py collectstatic --noinput && gunicorn socialmanager.wsgi:application
