import json
import pathlib

from django.core.management import BaseCommand
from django.db import connection

from mailing.models import Client, MailingText, Mailing, Status
from users.models import User

ROOT = pathlib.Path(__file__).parent.parent.parent.parent
DATA_CLIENT = pathlib.Path(ROOT, 'json_data', 'client.json')
DATA_MAILINGTEXT = pathlib.Path(ROOT, 'json_data', 'mailingtext.json')
DATA_MAILING = pathlib.Path(ROOT, 'json_data', 'mailing.json')
DATA_STATUS = pathlib.Path(ROOT, 'json_data', 'status.json')


class Command(BaseCommand):

    @staticmethod
    def json_read(path) -> list:
        # Здесь мы получаем данные из фикстур
        with open(path) as file:
            file_info = json.load(file)
        return [info for info in file_info]

    def handle(self, *args, **options):
        # Очистка базы данных перед заполнением
        Client.objects.all().delete()
        MailingText.objects.all().delete()
        Mailing.objects.all().delete()
        Status.objects.all().delete()

        client_for_create = []
        mailingtext_for_create = []
        mailing_for_create = []
        status_for_create = []

        with connection.cursor() as cursor:
            cursor.execute(
                "TRUNCATE TABLE mailing_client, mailing_mailingtext, mailing_mailing,"
                "mailing_status RESTART IDENTITY CASCADE;")

        for client in Command.json_read(DATA_CLIENT):
            client_fields = client.get('fields')
            client_for_create.append(
                Client(name=client_fields.get('name'),
                       email=client_fields.get('email'),
                       comment=client_fields.get('comment'))
            )

        Client.objects.bulk_create(client_for_create)

        for mailingtext in Command.json_read(DATA_MAILINGTEXT):
            mailingtext_fields = mailingtext.get('fields')
            mailingtext_for_create.append(
                MailingText(theme=mailingtext_fields.get('theme'),
                            body=mailingtext_fields.get('body'))
            )
        MailingText.objects.bulk_create(mailingtext_for_create)

        for mailing in Command.json_read(DATA_MAILING):
            mailing_fields = mailing.get('fields')
            mailing_for_create.append(
                Mailing(start_time=mailing_fields.get('start_time'),
                        end_time=mailing_fields.get('end_time'),
                        frequency=mailing_fields.get('frequency'),
                        status_of_mailing=mailing_fields.get('status_of_mailing'),
                        is_active=mailing_fields.get('is_active'),
                        owner=User.objects.get(pk=mailing_fields.get('owner')),
                        clients=Client.objects.filter(pk__in=mailing_fields.get('clients')),
                        mail=MailingText.objects.filter(pk__in=mailing_fields.get('mail')),)
            )
        Mailing.objects.bulk_create(mailing_for_create)

        for status in Command.json_read(DATA_STATUS):
            status_fields = status.get('fields')
            status_for_create.append(
                Status(last_attempt=status_fields.get('last_attempt'),
                       last_attempt_status=status_fields.get('last_attempt_status'),
                       client=User.objects.get(pk=status_fields.get('client')),
                       mailing_list=Mailing.objects.get(pk=status_fields.get('mailing_list')),
                       server_response=status_fields.get('server_response'))
            )
        Status.objects.bulk_create(status_for_create)
