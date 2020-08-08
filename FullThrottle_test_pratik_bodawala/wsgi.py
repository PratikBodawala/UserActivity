"""
WSGI config for FullThrottle_test_pratik_bodawala project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FullThrottle_test_pratik_bodawala.settings')

application = get_wsgi_application()
