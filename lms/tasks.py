from smtplib import SMTPException

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def sendmail(recipient):  # отправка письма
    status = False
    try:
        response = send_mail(
            'lms mailing',
            'course updated',
            settings.EMAIL_HOST_USER,
            (recipient,),
            fail_silently=False)
        status = True
    except SMTPException as err:  # ошибка SMTP
        response = 'Произошла ошибка при отправке письма' + str(err)
    except:  # другие ошибки
        response = "Отправка почты не удалась"
    return status, response

