import logging

import os
import django
from django.core.management.base import BaseCommand

from mailing.crontab import do

logger = logging.getLogger(__name__)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
django.setup()


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Вызываем команду напрямую
        do()
