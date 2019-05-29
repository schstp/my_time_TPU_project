from .base import *
from .base import get_secret

DEBUG = True

SECRET_KEY = get_secret('DJANGO_SECRET_KEY')

ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
]

# EMAIL
# ------------------------------------------------------------------------------
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'myTime.help.team@gmail.com'
EMAIL_HOST_PASSWORD = get_secret('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'myTime.help.team@gmail.com'