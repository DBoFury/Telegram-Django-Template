from django.core.management.base import BaseCommand
from bot.bot import run_pooling


class Command(BaseCommand):
    help = 'Run bot in pooling mode'

    def handle(self, *args, **options):
        run_pooling()
