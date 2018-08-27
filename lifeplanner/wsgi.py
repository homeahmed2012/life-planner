"""
WSGI config for lifeplanner project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os, sys
# add the hellodjango project path into the sys.path
sys.path.append('/var/www/html/lifeplanner')

# # add the virtualenv site-packages path to the sys.path
sys.path.append('/home/ammma/anaconda3/lib/python3.6/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lifeplanner.settings")
# django.setup(set_prefix=False)

application = get_wsgi_application()
