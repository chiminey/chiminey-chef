#Generated from Chef, do not modify
from bdphpcprovider.settings_changeme import *

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
            'filename': '/var/log/cloudenabling/bdphpcprovider.log',
            'formatter': 'timestamped',
            'maxBytes': 1024 * 1024 * 100,  # 100 mb
            'backupCount': 2
        },
        'celeryd': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/cloudenabling/celery/celeryd.log',
            'formatter': 'celery',
            'maxBytes': 1024 * 1024 * 100,  # 100 mb
            'backupCount': 2
        },
    },
    'loggers': {
        'bdphpcprovider.smartconnectorscheduler': {
            'level': 'WARN',
            'handlers': ['file'],
            },
        'bdphpcprovider.reliabilityframework': {
            'level': 'WARN',
                'handlers': ['file'],
            },
        'bdphpcprovider.simpleui': {
            'level': 'WARN',
                'handlers': ['file'],
            },
        'bdphpcprovider.core': {
            'level': 'WARN',
                'handlers': ['file'],
            },
        'bdphpcprovider.smartconnectorscheduler.tasks': {
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