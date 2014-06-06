"""
WSGI config for gestograma project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys
sys.path = ['/var/www/GTG/gestograma'] + sys.path
os.environ['DJANGO_SETTINGS_MODULE'] = 'gestograma.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
