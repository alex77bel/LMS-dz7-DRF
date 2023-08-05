from datetime import timedelta

from django.utils import timezone
from rest_framework import viewsets

from lms.tasks import sendmail

from lms.models import Course, Subscription
from lms import serializers
from lms.paginators import CustomPaginator
from lms.permissions import CoursePermissions
from lms.views.lesson_views import GetModeratorOrOwnerMixin, SetOwnerMixin


class CourseViewSet(SetOwnerMixin, GetModeratorOrOwnerMixin, viewsets.ModelViewSet):
    serializer_class = serializers.CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [CoursePermissions]
    pagination_class = CustomPaginator

    def update(self, request, *args, **kwargs):
        """Обработка обновления курса"""
        course = self.queryset.get(pk=kwargs['pk'])  # текущий курс

        # Обновить курс можно не чаще 1 раза в 4 часа, с рассылкой
        if timezone.now() - course.last_update > timedelta(hours=4):
            course.last_update = timezone.now()  # сохранение времени обновления в бд
            course.save()
            # выбор подписок с текущим курсом
            subscriptions = Subscription.objects.filter(course=course)
            for subscription in subscriptions:
                if subscription.is_subscribed:  # если подписка активна
                    recipient = str(subscription.owner)  # выбор владельца подписки
                    sendmail.delay(recipient)  # асинхронная рассылка
        return super().update(request, *args, **kwargs)
