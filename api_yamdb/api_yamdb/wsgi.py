# import os
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE',
# 'api_yamdb.api_yamdb.settings')

import os
import sys

from django.core.wsgi import get_wsgi_application

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.development'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.development")
application = get_wsgi_application()
