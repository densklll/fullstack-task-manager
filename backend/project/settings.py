import os
from pathlib import Path
import rest_framework.serializers

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'replace-me-with-a-secure-key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'apps.tasks',  # наше приложение с задачами
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates' ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

# Database (используем SQLite для демонстрации, можно заменить на PostgreSQL/MySQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = []

# Internationalization
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, etc.)
STATIC_URL = '/static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django REST Framework конфигурация
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

# Celery конфигурация
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# Monkey patch для устранения проблемы с отсутствующим NullBooleanField в DRF 3.14
if not hasattr(rest_framework.serializers, 'NullBooleanField'):
    rest_framework.serializers.NullBooleanField = rest_framework.serializers.BooleanField 
# 2023-01-16: Sketch serializer deadline optional field (prod checklist)

# 2023-01-28: Capture DRF pagination cursor vs offset (demo box)

# 2023-02-07: Stub gunicorn worker count on dev (staging)

# 2023-02-20: Capture axios 401 refresh race (local dev)

# 2023-02-28: Align gunicorn worker count on dev (local dev)

# 2023-03-15: Tighten Celery task idempotency key (CI runner)

# 2023-03-30: Describe docker compose service links (staging)

# 2023-04-15: Stub Redux task normalization (demo box)

# 2023-04-28: Document DRF pagination cursor vs offset (prod checklist)

# 2023-05-11: Tighten chart tooltip empty dataset (local dev)

# 2023-06-01: Record docker compose service links (staging)

# 2023-06-17: Capture gunicorn worker count on dev (CI runner)

# 2023-07-03: Sketch frontend env base URL (demo box)
