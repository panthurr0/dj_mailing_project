from datetime import timedelta

from mailing.models import Mailing, CREATE, IN_WORK, DAILY, WEEKLY, MONTHLY
from mailing.services import send_mailing


def create_task_for_frequency(frequency, interval):
    mailings = Mailing.objects.prefetch_related('clients', 'mail').filter(
        frequency=frequency, status_of_mailing__in=[CREATE, IN_WORK], answer=True
    )
    if mailings.exists():
        for mail in mailings:
            send_mailing(mail)
            mail.start_time += timedelta(days=interval)
            mail.save()


def create_daily_task():
    create_task_for_frequency(DAILY, 1)


def create_weekly_task():
    create_task_for_frequency(WEEKLY, 7)


def create_monthly_task():
    create_task_for_frequency(MONTHLY, 30)
