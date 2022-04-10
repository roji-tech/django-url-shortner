from .main_conf import *
# import django_heroku
# import dj_database_url

SECRET_KEY = 'pax!e5sxl*q&#_ic*m$*3#)#r)naw_4roumm@10x#iyg10c4zomq'

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': dj_database_url.config()
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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
django_heroku.settings(locals())