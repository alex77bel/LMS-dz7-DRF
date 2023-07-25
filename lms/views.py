from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter

from lms.models import Course, Lesson, Payment
from lms import serializers


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CourseSerializer
    queryset = Course.objects.all()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    serializer_class = serializers.LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = serializers.LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.PaymentSerializer


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = serializers.PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]  # настройки фильтрации и сортировки
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method')  # настройки фильтрации
    ordering_fields = ('paid_at',)  # настройки сортировки


class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.PaymentSerializer
    queryset = Payment.objects.all()


class PaymentUpdateAPIView(generics.UpdateAPIView):
    serializer_class = serializers.PaymentSerializer
    queryset = Payment.objects.all()


class PaymentDestroyAPIView(generics.DestroyAPIView):
    queryset = Payment.objects.all()
