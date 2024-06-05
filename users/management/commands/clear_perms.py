from django.core.management import BaseCommand
from django.db import connection


class Command(BaseCommand):
    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute(
                "TRUNCATE TABLE auth_permission, auth_group "
                "RESTART IDENTITY CASCADE;")