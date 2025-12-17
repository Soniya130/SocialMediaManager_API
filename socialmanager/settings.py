import os
import dj_database_url
from pathlib import Path
import dj_database_url
ROOT_URLCONF = 'socialmanager.urls'
WSGI_APPLICATION = 'socialmanager.wsgi.application'
ASGI_APPLICATION = 'socialmanager.asgi.application'

DATABASES = {
    "default": dj_database_url.config(default=os.environ.get("DATABASE_URL"))
}
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY", "2$)0rd-+-0159iva5qrv378)c_+p$&$hma_fhfo-i&72cy$7fs")

DEBUG = os.environ.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = [
    os.environ.get("RAILWAY_PUBLIC_DOMAIN", "localhost")
]


# Static files
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# Middleware for static files in production
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # ... keep other middleware
]
