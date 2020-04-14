from .defaults import *

DEBUG = True
ALLOWED_HOSTS += ['0.0.0.0', 'localhost', '127.0.0.1']

WSGI_APPLICATION = 'config.wsgi.dev.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'database/db.sqlite3'),
    }
}

CORS_ORIGIN_WHITELIST = (
    'localhost:3000',
    '127.0.0.1',
)
