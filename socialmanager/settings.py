import os
from pathlib import Path
import dj_database_url

# BASE_DIR defined once
BASE_DIR = Path(__file__).resolve().parent.parent

# Ensure staticfiles directory exists at startup
os.makedirs(BASE_DIR / "staticfiles", exist_ok=True)

# Secret key and debug
SECRET_KEY = os.environ.get(
    "SECRET_KEY", "2$)0rd-+-0159iva5qrv378)c_+p$&$hma_fhfo-i&72cy$7fs"
)
DEBUG = os.environ.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = [
    os.environ.get("RAILWAY_PUBLIC_DOMAIN", "localhost")
    "web-production-1504c.up.railway.app",
]

# Database
DATABASES = {
    "default": dj_database_url.config(default=os.environ.get("DATABASE_URL"))
}

# URLs / WSGI / ASGI
ROOT_URLCONF = "socialmanager.urls"
WSGI_APPLICATION = "socialmanager.wsgi.application"
ASGI_APPLICATION = "socialmanager.asgi.application"

# Static files
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Middleware
MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Installed apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",
    "social_posts.apps.SocialPostsConfig",
]
