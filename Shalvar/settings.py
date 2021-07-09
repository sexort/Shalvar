from pathlib import Path
from sys import exit

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-z^%h08*z%vs&0d^d-go89n$v+96m+^a0k^(48r)+e#abr_g0q8'

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'shalvar_installer',
    'user_auth',
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

ROOT_URLCONF = 'Shalvar.urls'

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

WSGI_APPLICATION = 'Shalvar.wsgi.application'
try:
    import database
    if database.database_type == "mysql":
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': database.database_name,
                'USER': database.database_username,
                'PASSWORD': database.database_password,
                'HOST': 'localhost',
                'PORT': database.database_port,
            }
        }

    elif database.database_type == "postgresql":
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': database.database_name,
                'USER': database.database_username,
                'PASSWORD': database.database_password,
                'HOST': 'localhost',
                'PORT': database.database_port,
            }
        }

    elif database.database_type == "mongodb":
        DATABASES = {
            'default': {
                'ENGINE': 'djongo',
                'NAME': database.database_name,
                'ENFORCE_SCHEMA': False,
                'CLIENT': {
                    'host': f'mongodb+sev://{database.database_username}:{database.database_password}@localhost/'
                            f'{database.database_name}?retryWrites=true&w=majority'
                }
            }
        }

    elif database.database_type == "sqlite":
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
except ImportError:
    print("Define database.py file")
    exit(True)


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
