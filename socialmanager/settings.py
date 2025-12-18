import os
from pathlib import Path
import dj_database_url

# BASE_DIR defined once
BASE_DIR = Path(__file__).resolve().parent.parent


# Secret key and debug
SECRET_KEY = os.environ.get(
    "SECRET_KEY", "2$)0rd-+-0159iva5qrv378)c_+p$&$hma_fhfo-i&72cy$7fs"
)
DEBUG = os.environ.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = [
    os.environ.get("RAILWAY_PUBLIC_DOMAIN", "localhost"),
    "web-production-1504c.up.railway.app",
    '127.0.0.1',
]
CSRF_TRUSTED_ORIGINS = [
    "https://web-production-1504c.up.railway.app",
]
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True



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
STATICFILES_DIRS = [BASE_DIR / "static"]  # Only if you have global static folder
# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

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
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # optional, create a 'templates' folder
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]