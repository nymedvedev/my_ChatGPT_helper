"""
Django settings for ChatGPT_site project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
from pathlib import Path
import os
# библиотека для хранения SECRET_KEY и DATABASES PASSWORD во внешней среде (.env)
# вместо хранения в данном файле:
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()
# SECURITY WARNING: keep the secret key used in production secret!
# Получаем SECRET_KEY из переменной окружения
SECRET_KEY = os.getenv('SECRET_KEY')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = bool(os.environ.get('DJANGO_DEBUG', True))

# '127.0.0.1' - хост домашнего (локального) сервера.
ALLOWED_HOSTS = ['127.0.0.1'] # коммерческий хост удалён !!!
# CSRF_TRUSTED_ORIGINS = [] # коммерческий сайт удалён !!!


# Application definition

INSTALLED_APPS = [
    # мои приложения:
    'users',
    'ChatGPT_site',
    'forms',
    # приложения Django:
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

ROOT_URLCONF = 'ChatGPT_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates/'],
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

WSGI_APPLICATION = 'ChatGPT_site.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru-RU'
# Установка часового пояса по умолчанию:
TIME_ZONE = 'UTC'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
# ПОДКЛЮЧАЮ ВОЗМОЖНОСТЬ ИСП. СТАТИКИ (ФАЙЛОВ С HDD)
STATICFILES_DIRS = [
    BASE_DIR / "static"
]
# ДОБАВИЛ ВОЗМОЖНОСТЬ ИСПОЛЬЗОВАНИЯ МЕДИА-ФАЙЛОВ:
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# при входе в систему редирект будет на страничку с name='ChatGPT_helper'
LOGIN_REDIRECT_URL = 'ChatGPT_helper'

# чтобы Джанго не падал при отсутствии '/' в конце URL при POST-запросе:
APPEND_SLASH = False

# установил необх. библиотеки для использ. асинхронного кода:
# pip install channels aiohttp asyncio
# и устанавливаю соотв. значение в settings, чтобы использовался asgi.py (вместо wsgi.py)
ASGI_APPLICATION = "ChatGPT_site.asgi.application"

# Конфигурация подключения к базе данных:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': None, # КОММЕРЧЕСКИЕ ДАННЫЕ ЗАМЕНЕНЫ НА None !!!
        'USER': None, # для запуска на локальном сервере использовать DATABASES из кода ниже !!!
        # Получаем PASSWORD из переменной окружения:
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': None,
        'PORT': None,
        'OPTIONS': {
            # SQL-запрос, который устанавливает режим работы MySQL в строгом режиме транзакций:
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4'
        },
    }
}

# Конфигурация подкл. к БД по-умолчанию:
"""
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
"""

# включаем учёт часовых поясов для столбца timestamp в БД:
USE_TZ = True
USE_L10N = True
USE_I18N = True
