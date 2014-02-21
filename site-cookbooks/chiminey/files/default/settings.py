#Generated from Chef, do not modify
from chiminey.settings_changeme import *

DEBUG=False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bdphpc',
        'USER': 'bdphpc',
        'PASSWORD': 'bdphpc', # unused with ident auth
        'HOST': '',
        'PORT': '',
    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'timestamped': {
            'format': ' [%(asctime)s: %(levelname)s/%(processName)s] %(message)s'
           # 'format': '%(asctime)s-%(filename)s-%(lineno)s-%(levelname)s: %(message)s'
        },
    'celery': {
            'format': ' [%(asctime)s: %(levelname)s/%(task_name)s] %(message)s'
    }

    },

    'handlers': {
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/chiminey/chiminey.log',
            'formatter': 'timestamped',
            'maxBytes': 1024 * 1024 * 100,  # 100 mb
            'backupCount': 2
        },
        'celeryd': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/chiminey/celery/celeryd.log',
            'formatter': 'celery',
            'maxBytes': 1024 * 1024 * 100,  # 100 mb
            'backupCount': 2
        },
    },
    'loggers': {
        'chiminey.smartconnectorscheduler': {
            'level': 'WARN',
            'handlers': ['file'],
            },
        'chiminey.reliabilityframework': {
            'level': 'WARN',
                'handlers': ['file'],
            },
        'chiminey.simpleui': {
            'level': 'WARN',
                'handlers': ['file'],
            },
        'chiminey.core': {
            'level': 'WARN',
                'handlers': ['file'],
            },
        'chiminey.smartconnectorscheduler.tasks': {
            'level': 'WARN',
            'handlers': ['celeryd'],
            },
        'celery.task': {
                'level': 'ERROR',
                'handlers': ['celeryd'],
            },
        'django.db.backends': {
                'level': 'WARN',
                'handlers': ['file'],
        },
}
}