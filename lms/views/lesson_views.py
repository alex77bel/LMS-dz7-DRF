from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from lms.models import Lesson
from lms import serializers
from lms.permissions import IsOwner


class GetModeratorOrOwnerMixin:
    """
    Возвращает queryset для модератора - полностью,
    для не модератора - только свои объекты
    """

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            return self.queryset.model.objects.all()
        else:
            return self.queryset.model.objects.all().filter(owner=self.request.user)


class LessonBaseMixin:
    """
    Базовый класс Lesson
    """

    serializer_class = serializers.LessonSerializer
    queryset = Lesson.objects.all()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.LessonSerializer

    def perform_create(self, serializer):  # получение текущего авторизованного пользователя
        new_lesson = serializer.save()
        new_lesson.user = self.request.user


class LessonListAPIView(GetModeratorOrOwnerMixin, LessonBaseMixin, generics.ListAPIView):
    permission_classes = [IsOwner | IsAdminUser]  # смотреть может только модератор или владелец


class LessonRetrieveAPIView(LessonBaseMixin, generics.RetrieveAPIView):
    permission_classes = [IsOwner | IsAdminUser]  # смотреть может только модератор или владелец


class LessonUpdateAPIView(LessonBaseMixin, generics.UpdateAPIView):  # менять может только владелец
    permission_classes = [IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):  # менять может только владелец
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner]
