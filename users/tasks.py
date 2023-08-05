from datetime import datetime, timedelta
from smtplib import SMTPException

from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from config import settings
from users.models import User


@shared_task()
def user_activity_check():
    """Проверка активности пользователя"""
    users = User.objects.all()
    for user in users:
        if user.last_login:
            if timezone.now() - user.last_login > timedelta(days=30):  # если не активен более 30 дней
                user.is_active = False  # деактивировать
                user.save()
