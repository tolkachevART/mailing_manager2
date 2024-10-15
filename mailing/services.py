import pytz
from datetime import timedelta, datetime
from django.conf import settings
from django.core.mail import send_mail
from mailing.models import Mailing, Logs
def my_job():
    day = timedelta(days=1)
    week = timedelta(days=7)
    month = timedelta(days=28)
    # mailings = Mailing.objects.all().filter(is_activated=True)
    zone = pytz.timezone(settings.TIME_ZONE)
    today = datetime.now(zone)
    mailings = Mailing.objects.all().filter(next_date__lte=today).filter(is_activated=True)
    for mailing in mailings:
        if mailing.status != 'finished':
            mailing.status = 'active'
            mailing.save()
            emails_list = [client.email for client in mailing.mail_to.all()]
            print(f'Рассылка {mailing.name} - начало {mailing.next_date}, конец {mailing.end_date}')
            result = send_mail(
                subject=mailing.message.topic,
                message=mailing.message.content,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=emails_list
            )
            status = result == True
            log = Logs(mailing=mailing, status=status)
            log.save()
            if status:  # на случай сбоя рассылки она останется активной
                if mailing.next_date < mailing.end_date:
                    mailing.status = 'created'
                else:
                    mailing.status = 'finished'
            if mailing.interval == 'daily':
                mailing.next_date = log.last_datetime_sending + day
            elif mailing.interval == 'weekly':
                mailing.next_date = log.last_datetime_sending + week
            elif mailing.interval == 'monthly':
                mailing.next_date = log.last_datetime_sending + month
            elif mailing.interval == 'once':
                mailing.next_date = mailing.end_date
            mailing.save()
            print(f'Рассылка {mailing.name} отправлена {today} (должна была {mailing.next_date}'
                  f'')