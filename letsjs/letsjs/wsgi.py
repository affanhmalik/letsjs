"""
WSGI config for letsjs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "letsjs.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

import sys
sys.path.append('/home/ubuntu/letsjs/letsjs')
