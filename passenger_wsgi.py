# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u2240405/data/www/clicklinks.ru/clicklinks')
sys.path.insert(1, '/var/www/u2240405/data/venv/lib/python3.10/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'clicklinks.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
