from datetime import datetime

import pytz

from config import settings
from mailing.models import Mailing


def do():

    from mailing.create_task import create_daily_task, create_weekly_task, create_monthly_task
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    create_daily_task()
    create_weekly_task()
    create_monthly_task()
    mailing = Mailing.objects.all()
    for post in mailing:
        print(f'POST: {current_datetime}, {post.pk}, {post.status_of_mailing}')
