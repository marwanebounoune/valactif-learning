"""
Django settings for Valactif_Learning project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path
# from getsecret import get_secret

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ktmw&&tak^$#_9&3i9i++a*^*73245tz^k2k%gx_)p_pr9%(um'

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
    'Accounts.apps.AccountsConfig',
    'storages',
    'corsheaders',
    




]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'corsheaders.middleware.CorsPostCsrfMiddleware'
]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = [
    'http://google.com',
    'http://valactif-crm1.s3.amazonaws.com',
    'http://localhost:8000',
    'http://127.0.0.1:9000'
]

ROOT_URLCONF = 'Valactif_Learning.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'Valactif_Learning.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mydb1',
        'USER': 'postgres',
        'PASSWORD' : 'mixside',
        'HOST': 'localhost'
    }
}
AUTH_USER_MODEL="Accounts.User"



# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
print("OK", os.path.join(BASE_DIR, 'static'))
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# print("BASE_DIR2", BASE_DIR2)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
MEDIA_URL = '/images/'
MEDIA_ROOT = os.path.join(MEDIA_URL, 'static/images')
#S3 BUCKETS CONFIG
AWS_ACCESS_KEY_ID = 'AKIATCPZDSK3RXB7AF55'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'valactif-crm1'

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_REGION_NAME = "eu-west-3"
AWS_S3_SIGNATURE_VERSION = "s3v4"
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'





# AWS_ACCESS_KEY_ID = 'AKIATCPZDSK3RXB7AF55'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_S3_CUSTOM_DOMAIN = 'dvepu9ka3eyf8.cloudfront.net'
# AWS_S3_SECURE_URLS = True
# AWS_STORAGE_BUCKET_NAME = 'valactif-crm1'
# COMPRESS_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# AWS_IS_GZIPPED = True
# STATIC_URL = 'https://dvepu9ka3eyf8.cloudfront.net/'
# COMPRESS_URL = STATIC_URL
#############################################################################
# AWS_STORAGE_BUCKET_NAME = 'valactif-crm1'
# AWS_CLOUDFRONT_DOMAIN = 'dvepu9ka3eyf8.cloudfront.net'
# AWS_ACCESS_KEY_ID = 'AKIATCPZDSK3RXB7AF55'
# AWS_SECRET_ACCESS_KEY = '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'

# MEDIAFILES_LOCATION = 'media'
# MEDIA_ROOT = '/%s/' % MEDIAFILES_LOCATION
# MEDIA_URL = '//%s/%s/' % (AWS_CLOUDFRONT_DOMAIN, MEDIAFILES_LOCATION)
# DEFAULT_FILE_STORAGE = 'app.custom_storages.MediaStorage'

# STATICFILES_LOCATION = 'static'
# STATIC_ROOT = '/%s/' % STATICFILES_LOCATION
# STATIC_URL = '//%s/%s/' % (AWS_CLOUDFRONT_DOMAIN, STATICFILES_LOCATION)
# STATICFILES_STORAGE = 'app.custom_storages.StaticStorage'
























# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'





































# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.eu-west-3.amazonaws.com'
# AWS_DEFAULT_ACL = 'public-read'
# AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
# AWS_LOCATION = ''
# AWS_QUERYSTRING_AUTH = False
# MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'
# BASE_DIR2 = Path(__file__).resolve().parent.parent
# MEDIA_ROOT = os.path.join(BASE_DIR2, '')
# print("MEDIA_ROOT", MEDIA_ROOT)
# MEDIAFILES_STORAGE  = 'storages.backends.s3boto3.S3Boto3Storage'


# AWS_ACCESS_KEY_ID = os.getenv('AKIATCPZDSK3RXB7AF55')
# AWS_SECRET_ACCESS_KEY = os.getenv('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')
# AWS_STORAGE_BUCKET_NAME = 'valactif-crm1'
# AWS_S3_FILE_OVERWRITE = False
# AWS_DEFAULT_ACL = None
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.eu-west-3.amazonaws.com'
# AWS_DEFAULT_ACL = 'public-read'
# AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
# # AWS_LOCATION = 'static'
# AWS_QUERYSTRING_AUTH = False
# STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

'''
USE_S3 = os.getenv('USE_S3') == 'TRUE'

if USE_S3:
    AWS_ACCESS_KEY_ID = os.getenv('AKIATCPZDSK372JFDNOT')
    AWS_SECRET_ACCESS_KEY = os.getenv('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')
    AWS_STORAGE_BUCKET_NAME = os.getenv('valactif-crm1')
    AWS_S3_FILE_OVERWRITE = False
    AWS_DEFAULT_ACL = None
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    # AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    # AWS_DEFAULT_ACL = 'public-read'
    # AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    # AWS_LOCATION = 'static'
    # AWS_QUERYSTRING_AUTH = False
    # STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
    # STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
else:
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'Valactif_Learning/static')]
'''