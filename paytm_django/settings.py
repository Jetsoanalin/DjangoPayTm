"""
Django settings for paytm_django project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!k+--^y-e^e0r(!0e#=9nwf#0)+5x7+citq&9-f-zr&_+eet0r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'paytm.apps.PaytmConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'paytm_django.urls'

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

WSGI_APPLICATION = 'paytm_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'


#-----------  make these environment variables ------------------#

PAYTM_MERCHANT_KEY = '' # < your production KEY >
PAYTM_MERCHANT_ID = '' # < your production ID >
PAYTM_WEBSITE = 'DEFAULT'
PAYTM_URL = 'https://securegw.paytm.in/theia/processTransaction'
# HOST_URL = 'http://127.0.0.1:8000/'
# Heroku Config
HOST_URL = 'https://djangopaytm.herokuapp.com'
PAYTM_CALLBACK_URL = "response/"

if DEBUG:
    PAYTM_MERCHANT_KEY = 'B!Kt8E!uJRBKWm3d' # < your staging key >
    PAYTM_MERCHANT_ID = 'kllrJF29732196755225' # < your staging ID >
    PAYTM_WEBSITE = 'WEBSTAGING'
    PAYTM_URL = 'https://securegw-stage.paytm.in/theia/processTransaction'

#-----------  make these environment variables ------------------#
#     For staging :-

#     Card:
#     Card Number : Any Visa or Master Card
#     Expiration Month & Year : Any Future month and Year
#     CVV : 123
#     OTP : 123123


#     Wallet:
#     Mobile Number : 7777777777
#     Password : Paytm12345
#     OTP: 489871

#     Net Banking :
#     Bank : Andhra Bank
#     User : test
#     Password : test


# CORS_REPLACE_HTTPS_REFERER      = False
# HOST_SCHEME                     = "http://"
# SECURE_PROXY_SSL_HEADER         = None
# SECURE_SSL_REDIRECT             = False
# SESSION_COOKIE_SECURE           = False
# CSRF_COOKIE_SECURE              = False
# SECURE_HSTS_SECONDS             = None
# SECURE_HSTS_INCLUDE_SUBDOMAINS  = False
# SECURE_FRAME_DENY               = False

django_heroku.settings(locals())
