import os
from django.conf import settings

DEBUG = False
TEMPLATE_DEBUG = False

DATABASES = settings.DATABASES

import dj_database_url

# Parse database configuration from $DATABASE_URL
DATABASES['default'] =  dj_database_url.config()

if len(DATABASES['default']) == 0:
	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
	        'NAME': 'lwc',                      # Or path to database file if using sqlite3.
	        # The following settings are not used with sqlite3:
	        'USER': 'root',
	        'PASSWORD': '123',
	        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
	        'PORT': '',                      # Set to empty string for default.
	    }
	}


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

SHARE_URL = "http://launchwithcode.com/?ref="
