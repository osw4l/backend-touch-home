from .base import *

DEBUG = True

INSTALLED_APPS += ('gunicorn',)

ALLOWED_HOSTS = ['*']

AUTH_PASSWORD_VALIDATORS = [
   
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

WSGI_APPLICATION = 'project.wsgi.production.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db5m2khft89et6',
        'USER': 'fdimxosxljvsca',
        'PASSWORD': 'd480fd7e379f281793503e7d9ad011caa2ec32a5ef6442dc456873affba369ec',
        'HOST': 'ec2-75-101-142-91.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
