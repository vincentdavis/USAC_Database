from .base import *

if 'RDS_DB_NAME' in os.environ and os.environ['RDS_DB_NAME']:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }


if CURRENT_ENV == ENV_PRODUCTION:
    STATIC_ROOT = os.path.join(BASE_DIR, "www", "static")
