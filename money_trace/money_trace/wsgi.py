"""
WSGI config for money_trace project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""
import os
import sys
#
## assuming your django settings file is at '/home/MoneyTrace/mysite/mysite/settings.py'
## and your manage.py is is at '/home/MoneyTrace/mysite/manage.py'
path = '/home/Moneey/MONEY_TRACE/money_trace'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'money_trace.settings'
#
## then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


