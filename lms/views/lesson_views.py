from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from lms.models import Lesson
from lms import serializers
from lms.paginators import CustomPaginator
from lms.permissions import IsOwner


class SetOwnerMixin:
    def perform_create(self, serializer):  # получение текущего авторизованного пользователя
        new_obj = serializer.save()
        new_obj.owner = self.request.user
        new_obj.save()


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


class LessonCreateAPIView(SetOwnerMixin, generics.CreateAPIView):
    serializer_class = serializers.LessonSerializer


class LessonListAPIView(GetModeratorOrOwnerMixin, LessonBaseMixin, generics.ListAPIView):
    permission_classes = [IsOwner | IsAdminUser]  # смотреть может только модератор или владелец
    pagination_class = CustomPaginator


class LessonRetrieveAPIView(LessonBaseMixin, generics.RetrieveAPIView):
    permission_classes = [IsOwner | IsAdminUser]  # смотреть может только модератор или владелец


class LessonUpdateAPIView(LessonBaseMixin, generics.UpdateAPIView):  # менять может только владелец
    permission_classes = [IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):  # менять может только владелец
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner]
