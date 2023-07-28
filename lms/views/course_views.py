from rest_framework import viewsets

from lms.models import Course
from lms import serializers


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CourseSerializer
    queryset = Course.objects.all()
