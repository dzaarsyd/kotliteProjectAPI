"""
Django settings for kotliteProjectAPI project.

Generated by 'django-admin startproject' using Django 3.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ctf(%ivp_tr&k&-%5)3r(k7@w&k86xf@v^k)q5u+wf7h4$q#^!'

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
    'api',
    'coreapi'
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

ROOT_URLCONF = 'kotliteProjectAPI.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'kotliteProjectAPI.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# Install PyMySQL as mysqlclient/MySQLdb to use Django's mysqlclient adapter
# See https://docs.djangoproject.com/en/3.2/ref/databases/#mysql-db-api-drivers
# for more information

# UNCOMMENT THIS CODE FOR SETUP IN GCP
# import pymysql  # noqa: 402
# pymysql.version_info = (2, 0, 3, 'final', 0)  # change mysqlclient version
# pymysql.install_as_MySQLdb()


# [START db_setup]
# if os.getenv('GAE_APPLICATION', None):
#     # Running on production App Engine, so connect to Google Cloud SQL using
#     # the unix socket at /cloudsql/<your-cloudsql-connection string>
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.mysql',
#             'HOST': '/cloudsql/[YOUR-CONNECTION-NAME]',
#             'USER': '[YOUR-USERNAME]',
#             'PASSWORD': '[YOUR-PASSWORD]',
#             'NAME': '[YOUR-DATABASE]',
#         }
#     }
# else:
#     # Running locally so connect to either a local MySQL instance or connect to
#     # Cloud SQL via the proxy. To start the proxy via command line:
#     #
#     #     $ cloud_sql_proxy -instances=[INSTANCE_CONNECTION_NAME]=tcp:3306
#     #
#     # See https://cloud.google.com/sql/docs/mysql-connect-proxy
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.mysql',
#             'HOST': '127.0.0.1',
#             'PORT': '3306',
#             'NAME': '[YOUR-DATABASE]',
#             'USER': '[YOUR-USERNAME]',
#             'PASSWORD': '[YOUR-PASSWORD]',
#         }
#     }
# [END db_setup]

# UNCOMMENT THIS CODE FOR LOCAL TESTING
# Use a in-memory sqlite3 database when testing in CI systems
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
