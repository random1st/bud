import environ

env = environ.Env(DEBUG=(bool, False),)
env.read_env()

base_dir = environ.Path(__file__) - 1

DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = env('ALLOWED_HOSTS', default=[])
SITE_ID = 1

BUILTIN_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

LOCAL_APPS = (
    'users',
)

THIRD_PARTY_APPS = (
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
)

INSTALLED_APPS = BUILTIN_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

# Entry points
ROOT_URLCONF = '{{ cookiecutter.project_name }}.urls'
WSGI_APPLICATION = '{{ cookiecutter.project_name }}.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    base_dir('static'),
)
STATIC_ROOT = base_dir('static_all')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            base_dir('templates'),
        ],
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

# Attached resources
DATABASES = {
    'default': env.db(),
}

# Users
AUTH_USER_MODEL = 'users.User'
LOGIN_REDIRECT_URL = 'index'
LOGIN_URL = 'account_login'
ADMIN_URL = r'^admin/'

# Authentication
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_ADAPTER = 'users.adapter.AccountAdapter'
ACCOUNT_ALLOW_REGISTRATION = True
ACCOUNT_SESSION_REMEMBER = True
SOCIALACCOUNT_ADAPTER = 'users.adapter.SocialAccountAdapter'
