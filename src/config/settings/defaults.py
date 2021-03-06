import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '-05sgp9!deq=q1nltm@^^2cc+v29i(tyybv3v2t77qi66czazj'
DEBUG = True
ALLOWED_HOSTS = []

TEMPLATE_DIR = os.path.join(os.path.dirname(BASE_DIR), 'templates')
STATIC_FILE_DIR = os.path.join(os.path.dirname(BASE_DIR), 'static')

TEMPLATE_CONTEXT_PROCESSORS = (
   "django.template.context_processors.request",
)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'Secretary.apps.SecretaryConfig',
    'instructor.apps.InstructorConfig',
    'Student.apps.StudentConfig',
    'planning.apps.PlanningConfig',
    'users.apps.UsersConfig',

    'phone_field',
    'ckeditor',
    'crispy_forms',
    'colorfield'


]
CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 'debug_toolbar.middleware.DebugToolbarMiddleware'
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (TEMPLATE_DIR,),
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


AUTH_USER_MODEL = 'users.User'
# ACCOUNT_UNIQUE_EMAIL = True
# AUTH_USER_MODEL = "Secretary.User"

LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = (STATIC_FILE_DIR, )
# STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static/assets/css/main.css")
