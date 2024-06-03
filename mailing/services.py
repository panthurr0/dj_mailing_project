from datetime import datetime
from smtplib import SMTPException

import pytz
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect

from mailing.models import Status, Mailing, DONE, IN_WORK


def send_mailing(mailing):
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    current_time_formatted = current_datetime.strftime("%Y-%m-%d %H:%M:%S%z")
    time_obj = datetime.strptime(current_time_formatted, "%Y-%m-%d %H:%M:%S%z")

    # Проверяем, должна ли рассылка выполняться в данный момент времени
    if mailing.start_time <= time_obj <= mailing.end_time:
        try:
            for client in mailing.clients.all():
                for post in mailing.message.all():
                    result = send_mail(
                        subject=post.subject,
                        message=post.text,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[client.contact_email],
                        fail_silently=False,
                    )
                    status = Status.objects.create(
                        time_attempt=current_datetime,
                        status_of_last_attempt=bool(result),
                        server_response="OK" if result else "Error",
                        mailing_list=mailing,
                        client=client,
                    )
                    status.save()

        except SMTPException as error:
            # Если произошла ошибка при отправке, создаем объект Log с соответствующими данными
            status = Status.objects.create(
                time_attempt=current_datetime,
                status_of_last_attempt=False,
                server_response=str(error),
                mailing_list=mailing,
            )
            status.save()
        if mailing.end_time <= time_obj:
            mailing.status_of_newsletter = DONE
        elif mailing.end_time >= time_obj:
            mailing.status_of_newsletter = IN_WORK

    mailing.save()
    print(6)


def toggle_activity(request, pk):
    mailing = Mailing.objects.get(pk=pk)
    if mailing.is_active:
        mailing.is_active = False
    else:
        mailing.is_active = True

    mailing.save()
    return redirect("mailing:mailing_list")
