from . base import *

SECRET_KEY = 'mySecretKey'

DEBUG = True

ALLOWED_HOSTS = ['*']

CORS_ALLOW_ALL_ORIGINS = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'snippetclass_development',
        'USER': 'snippetclass',
        'PASSWORD': 'snippetclass',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_VERIFICATION_LINK = 'http://127.0.0.1:8000/api/auth/verify_email'
