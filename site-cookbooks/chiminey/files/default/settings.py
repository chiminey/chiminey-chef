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
    },

    'handlers': {
    'file': {
    'class': 'logging.handlers.RotatingFileHandler',
    'filename': '/var/log/chiminey/chiminey.log',
    'formatter': 'timestamped',
            'maxBytes': 1024 * 1024 * 100,  # 100 mb
            'backupCount': 2
            },
    },
    'loggers': {

    'chiminey': {
    'level': 'WARN',
    'handlers': ['file'],
    },
    'chiminey.smartconnectorscheduler': {
    'level': 'WARN',
    'handlers': ['file'],
    },
    'chiminey.sshconnection': {
    'level': 'WARN',
    'handlers': ['file'],
    },
    'chiminey.platform': {
    'level': 'WARN',
    'handlers': ['file'],
    },
    'chiminey.cloudconnection': {
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
    'chiminey.mytardis': {
    'level': 'WARN',
    'handlers': ['file'],
    },
    'chiminey.simpleui.wizard': {
    'level': 'WARN',
    'handlers': ['file'],
    },
    'chiminey.storage': {
    'level': 'WARN',
    'handlers': ['file'],
    },
    'chiminey.sshconnector': {
    'level': 'WARN',
    'handlers': ['file'],
    },
    'chiminey.core': {
    'level': 'WARN',
    'handlers': ['file'],
    },
    'chiminey.smartconnectorscheduler.tasks': {
    'level': 'WARN',
    'handlers': ['file'],
    },
    'celery.task': {
    'level': 'WARN',
    'handlers': ['file'],
    },
    'django.db.backends': {
    'level': 'WARN',
    'handlers': ['file'],
    },
}
}

