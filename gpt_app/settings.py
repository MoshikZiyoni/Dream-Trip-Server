"""
Django settings for gpt_app project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y=8!%^v9_=x$&#z_t%5cp_$*te6jaemndo%&id9pn&4v3(&py&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = [
'accept',
'accept-encoding',
'authorization',
'content-type',
'dnt',
'origin',
'user-agent',
'x-csrftoken',
'x-requested-with',
]

CORS_ALLOW_METHODS = [
'DELETE',
'GET',
'OPTIONS',
'PATCH',
'POST',
'PUT',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'rest_framework',
    'corsheaders',
    'whitenoise.runserver_nostatic',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    "corsheaders.middleware.CorsPostCsrfMiddleware",
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",

]

ROOT_URLCONF = 'gpt_app.urls'
CORS_ORIGIN_ALLOW_ALL = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'gpt_app.wsgi.application'
ASGI_APPLICATION = 'gpt_app.asgi.application'
ASGI_APPLICATION_OPTIONS = {
    'timeout': 120,
}


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# Render
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'dreamtrip_mhc6', 
#         'USER': 'moshik', 
#         'PASSWORD': 'aHOn2XVjQGdBne1yUMSs5X6SvrD1GOKt',
#         'HOST': 'dpg-cgpu7kheuhlq287lbmpg-a.frankfurt-postgres.render.com', 
#         'PORT': '5432',
#     }
# }

###MYSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'moshik_liran',
        'HOST':'dream-trip-database.ceyknkppkpg5.eu-north-1.rds.amazonaws.com',
        'USER': 'admin',
        'PASSWORD': 'Theking1!',
        'PORT':'3306',
    },
}

# '''
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
# '''
# ###  'MONGODB'
# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': 'tripdatabase'
# ,
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/images/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_ROOT = os.path.join(BASE_DIR, 'staticfiles/images')
# MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images/')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOW_ORIGIN = ['*',"http://localhost:3000"]


CSRF_COOKIE_HTTPONLY = True

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
CELERY_IMPORTS = ['app.tasks']