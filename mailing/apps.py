from django.apps import AppConfig
from django.conf import settings


class MailingConfig(AppConfig):
    default_auto_field = settings.DEFAULT_AUTO_FIELD
    name = 'mailing'
    verbose_name = 'рассылки'

    # def ready(self):
    #     from mailing.crontab import do
    #     do()
