import os
from django.conf import settings

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = settings.DATABASES

import dj_database_url

# Parse database configuration from $DATABASE_URL
DATABASES['default'] =  dj_database_url.config()
DATABASE_TYPE = 'sqlite3'

print "len(DATABASES['default']) is : %s" % len(DATABASES['default'])

if len(DATABASES['default']) == 0:
    if DATABASE_TYPE == 'sqlite3':
		DATABASES = {
			'default': {
				'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
				'NAME': os.path.join(os.path.dirname(os.path.dirname(__file__)),'lwc.db'),                      # Or path to database file if using sqlite3.
			}
		}
    else:
		DATABASES = {
			'default': {
				'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
				'NAME': 'lwc',                      # Or path to database file if using sqlite3.
				# The following settings are not used with sqlite3:
				'USER': 'postgres',
				'PASSWORD': '123',
				'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
				'PORT': '',                      # Set to empty string for default.
			}
		}
    print "use postgresql_psycopg2 local "
else:
	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
	        'NAME': 'dbv6n78stkmeqg',                      # Or path to database file if using sqlite3.
	        # The following settings are not used with sqlite3:
	        'USER': 'ntccscinrvwneo',
	        'PASSWORD': ' TJG0ByhrZ5f412ZR6u4AnWUQoy',
	        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
	        'PORT': '5432',                      # Set to empty string for default.
	    }
	}
	print "use postgresql_psycopg2 server"


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

SHARE_URL = "http://launchwithcode.com/?ref="
