from .defaults import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'database/db.sqlite3'),
    }
}

ALLOWED_HOSTS = ['0.0.0.0', 'localhost']

SECRET_KEY = 'yy1(ruls3vkcfz%)-rafx_rbgw%jm&@w+cdxrhi&hsek1^war4'
