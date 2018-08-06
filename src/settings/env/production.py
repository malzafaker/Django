# -*- coding:utf-8 -*-
import os

DEBUG = False

ALLOWED_HOSTS = [
    '*',
]
SITE_HOST = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST'),
        'PORT': int(os.getenv('POSTGRES_PORT')),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        }
    },
    'formatters': {
        'main_formatter': {
            'format': '%(levelname)s: %(name)-25s | Message: %(message)-12s | Detail: %(asctime)s; %(filename)s:%(lineno)d',
            'datefmt': "%Y-%m-%d %H:%M:%S",
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'main_formatter',
        },
        'production_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/main.log',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 7,
            'formatter': 'main_formatter',
            'filters': ['require_debug_false'],
        },
        'debug_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/main_debug.log',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 7,
            'formatter': 'main_formatter',
            'filters': ['require_debug_true'],
        },
        'null': {
            "class": 'logging.NullHandler',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['null', ],
        },
        'py.warnings': {
            'handlers': ['null', ],
        },
        '': {
            'handlers': ['console', 'production_file', 'debug_file'],
            'level': "DEBUG",
        },
    }
}
