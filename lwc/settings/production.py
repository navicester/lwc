import os
from django.conf import settings

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = settings.DATABASES

import dj_database_url

# Parse database configuration from $DATABASE_URL
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

SHARE_URL = "http://launchwithcode.com/?ref="
