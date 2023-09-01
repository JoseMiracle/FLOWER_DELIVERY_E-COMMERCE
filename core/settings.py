"""
Django settings for core project.

"""
import os
import dj_database_url
from datetime import timedelta
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = int(os.getenv("DEBUG"))

ALLOWED_HOSTS = ['*']

# ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(",")


# Application definition

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Local Apps
    "accounts",
    "flower_delivery",

    # THIRD PARTY APPS
    "drf_spectacular",
    "corsheaders",
    "whitenoise.runserver_nostatic",
    "rest_framework",
    "rest_framework.authtoken",
    "dj_rest_auth",
    "cloudinary_storage",
    "cloudinary",
    "django_extensions",
    
    
    # SOCIAL LOGINS
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "dj_rest_auth.registration",
    "allauth.socialaccount",

    # SOCIAL OAUTH PROVIDERS
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.apple",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

SITE_ID = 1  # NOTE: Changr this later

ROOT_URLCONF = "core.urls"

# REST_FRAMEWORK
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

# SIMPLEJWT SETTINGS
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,
    "AUTH_HEADER_TYPES": ("Bearer",),
}


# SPECTACULAR
SPECTACULAR_SETTINGS = {
    "TITLE": "FLOWER_DELIVERY(E-COMMERCE)",
    "DESCRIPTION": "AN API DELIVERYING FLOWER",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if DEBUG == 1:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

else:
    DATABASES = {"default": dj_database_url.parse(os.getenv("DATABASE_URL"))}



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.getenv("CLOUD_NAME"),
    "API_KEY": os.getenv("API_KEY"),
    "API_SECRET": os.getenv("API_SECRET"),
}

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR/ 'media')
# DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "accounts.User"

STORAGES = {
    "staticfiles": {"BACKEND": "whitenoise.storage.CompressedStaticFilesStorage"}
}

STATIC_URL = "/staticfiles/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")


# CORS SETTINGS

CORS_ALLOWED_ORIGINS = [
"https://kyiv-luxebouquets.webflow.io",
"http://localhost:5173",
]

CORS_ALLOW_METHODS = [
'DELETE',
'GET',
'OPTIONS',
'PATCH',
'POST',
'PUT',
]