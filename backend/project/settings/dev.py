from .base import *

DEBUG = True

MIDDLEWARE += [
    'commons.flushmidware.flushWare',
]

if 'default' not in DATABASES:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
