"""
Django settings for web_edtl project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-n@+($a$99&$7l1-^vu!$)3%as)@aabn4l8bj2#p6urd2m&@8bs'

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
    # 'livereload'
    'django.contrib.staticfiles',
    'imagekit',
    'django_summernote',
    'main',
    'notification',
    'departments',
    'announcement',
    'finance',
    'recruitment',
    'pagemanegament',
    'procurament',
    'product',
    'faq',
    'django_social_share',
    'appointment',
    'gallery',
    'event',
    'project',
    'custom',
    'report',
    'news',
    'profiles',
    'crispy_forms',
    'crispy_bootstrap5',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'livereload.middleware.LiveReloadScript',
]

AUTH_USER_MODEL = 'main.User'

ROOT_URLCONF = 'web_edtl.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'Templates'],
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

WSGI_APPLICATION = 'web_edtl.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'edtl2',
        'USER': 'admin',
        'PASSWORD': 'Leste_123',
        'HOST': 'database-kinos.cx862xedog9t.ap-southeast-1.rds.amazonaws.com',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dili'

USE_I18N = True

USE_L10N = True

USE_TZ = True


LOGIN_REDIRECT_URL = 'admin-dashboard'
LOGIN_URL = 'login'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'edtlep@gmail.com'
EMAIL_HOST_PASSWORD = 'edtlep#2022'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# CRISPY_TEMPLATE_PACK = 'Bootstrap4'
# CRISPY_ALLOWED_TEMPLATE_PACKS = (
#     'bootstrap', 'bootstrap4', 'bootstrap5')
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static_project')
]
STATIC_ROOT = os.path.join(os.path.dirname(
    BASE_DIR / 'web_edtl'), 'static_cdn', 'static_root')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

CELERY_BROKER_URL = 'redis://13.229.130.93:6379'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

X_FRAME_OPTIONS = "SAMEORIGIN"
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
