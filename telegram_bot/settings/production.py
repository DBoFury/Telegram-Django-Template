"""
Production Settings for Heroku
"""

import environ

from .local import *

env = environ.Env()

DEBUG = env.bool('DEBUG', False)

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

if "DATABASE_URL" in env:
    DATABASES['default'] = env.db('DATABASE_URL')
    DATABASES["default"]["ATOMIC_REQUESTS"] = True

if "REDIS_URL" in env:
    CELERY_BROKER_URL = env.str('REDIS_URL') + '/1'
    CELERY_RESULT_BACKEND = env.str('REDIS_URL') + '/1'
