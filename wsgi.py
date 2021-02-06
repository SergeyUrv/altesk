#!/usr/bin/env python
from os import environ
from django.core.handlers.wsgi import WSGIHandler

environ['DJANGO_SETTINGS_MODULE'] = environ.get(
    'DJANGO_SETTINGS_MODULE', 'settings')

application = WSGIHandler()