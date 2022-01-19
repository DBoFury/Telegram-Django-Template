release: django-admin migrate --noinput
web: gunicorn telegram_bot.wsgi:application
worker: celery -A telegram_bot worker -l info --without-gossip --without-mingle --without-heartbeat -Ofair --pool=solo
beat: celery -A telegram_bot beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
