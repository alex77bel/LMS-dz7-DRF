from django.db import models
from django.utils import timezone

from config import settings
from users.models import User


class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    description = models.CharField(max_length=255, verbose_name='описание')
    preview = models.ImageField(upload_to='course/', verbose_name='превью', null=True, blank=True)
    last_update = models.DateTimeField(verbose_name='время последнего обновления', default=timezone.now)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.SET_NULL,
                              related_name='course',
                              verbose_name='пользователь',
                              null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ('name',)


class Lesson(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    description = models.CharField(max_length=255, verbose_name='описание')
    preview = models.ImageField(upload_to='course/', verbose_name='превью', null=True, blank=True)
    video_link = models.URLField(verbose_name='ссылка на видео', null=True, blank=True)

    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, related_name='lesson',
                               verbose_name='курс')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.SET_NULL,
                              related_name='lesson',
                              verbose_name='пользователь',
                              null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ('name',)


class Payment(models.Model):
    class PaymentMethods(models.TextChoices):
        CASH = 'CA', 'Cash'
        TRANSFER = 'TR', 'Transfer'

    payment_id = models.CharField(max_length=100, verbose_name='идентификатор платежа у Stripe')
    payment_status = models.CharField(max_length=30, verbose_name='статус платежа', null=True, blank=True)
    paid_at = models.DateField(verbose_name='дата оплаты')
    paid_course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True,
                                    verbose_name='оплаченный курс')
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True, blank=True,
                                    verbose_name='оплаченный урок')
    payment_amount = models.PositiveIntegerField(verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=2,
                                      choices=PaymentMethods.choices,
                                      default=PaymentMethods.CASH,
                                      verbose_name='способ оплаты')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.SET_NULL,
                              related_name='payment',
                              verbose_name='пользователь',
                              null=True, blank=True)

    def __str__(self):
        return f'Дата платежа {self.paid_at}, размер платежа {self.payment_amount}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
        ordering = ('-paid_at',)


class Subscription(models.Model):
    is_subscribed = models.BooleanField(verbose_name='признак подписки', default=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               verbose_name='подписка на курс',
                               related_name='subscription')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.SET_NULL,
                              related_name='subscription',
                              verbose_name='пользователь',
                              null=True, blank=True)

    def __str__(self):
        return f'Subscription to {self.course} by {self.owner}'

    class Meta:
        verbose_name = 'Подписка на курс'
        verbose_name_plural = 'Подписки на курс'
        ordering = ('course',)
