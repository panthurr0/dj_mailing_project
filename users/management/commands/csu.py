from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='bla@mail.ru',  # USERNAME_FIELD = "email"
            is_staff=True,
            is_superuser=True,
            is_active=True
        )

        user.set_password('111')
        user.save()
