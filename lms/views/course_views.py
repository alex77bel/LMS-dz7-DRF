from rest_framework import viewsets

from lms.models import Course
from lms import serializers
from lms.permissions import CoursePermissions
from lms.views.lesson_views import GetModeratorOrOwnerMixin, SetOwnerMixin


class CourseViewSet(SetOwnerMixin, GetModeratorOrOwnerMixin, viewsets.ModelViewSet):
    serializer_class = serializers.CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [CoursePermissions]
