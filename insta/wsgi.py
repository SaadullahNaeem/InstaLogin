import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "insta.settings")
from django.conf import settings
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

if not settings.DEBUG:
    try:
        from whitenoise.django import DjangoWhiteNoise
        application = get_wsgi_application()
        application = DjangoWhiteNoise(application)
    except:
        pass