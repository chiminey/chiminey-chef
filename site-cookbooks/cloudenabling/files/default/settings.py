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
            'format': '%(asctime)s-%(filename)s-%(lineno)s-%(levelname)s: %(message)s'
        },
    },

    'handlers': {
        'file': {
            'level':'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/log/cloudenabling/bdphpcprovider.log',
            'formatter': 'timestamped'
        },
    },
    'loggers': {
        'bdphpcprovider.smartconnectorscheduler': {
            'handlers': ['file'],
            'level': 'INFO',
            },
        'bdphpcprovider.reliabilityframework': {
                'handlers': ['file'],
                'level': 'INFO',
            },
        'bdphpcprovider.simpleui': {
                'handlers': ['file'],
                'level': 'INFO',
            },
        'bdphpcprovider.core': {
                'handlers': ['file'],
                'level': 'INFO',
            },
        }
}


CELERY_DEFAULT_QUEUE = 'default'
CELERY_QUEUES = {
   "hightasks": {
       "binding_key": "high",
       "exchange": "default",
   },
   "default": {
       "binding_key": "default",
       "exchange": "default",
   }
}
CELERY_DEFAULT_EXCHANGE = "default"
CELERY_DEFAULT_EXCHANGE_TYPE = "direct"
CELERY_DEFAULT_ROUTING_KEY = "default"

CELERY_ROUTES = {
  "smartconnectorscheduler.context_message": {
   "queue": "hightasks",
   "routing_key": "high",
},
"smartconnectorscheduler.delete": {
   "queue": "hightasks",
   "routing_key": "high",
},
}

#BROKER_TRANSPORT = 'django'
BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
