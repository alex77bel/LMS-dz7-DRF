from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter

from lms.models import Payment
from lms import serializers
from lms.views.lesson_views import SetOwnerMixin


class PaymentBaseMixin:
    """
    Базовый класс Payment
    """
    serializer_class = serializers.PaymentSerializer
    queryset = Payment.objects.all()


class PaymentCreateAPIView(SetOwnerMixin, generics.CreateAPIView):
    serializer_class = serializers.PaymentCreateSerializer

class PaymentListAPIView(PaymentBaseMixin, generics.ListAPIView):
    filter_backends = [DjangoFilterBackend, OrderingFilter]  # настройки фильтрации и сортировки
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method')  # настройки фильтрации
    ordering_fields = ('paid_at',)  # настройки сортировки


class PaymentRetrieveAPIView(PaymentBaseMixin, generics.RetrieveAPIView):
    pass


class PaymentUpdateAPIView(PaymentBaseMixin, generics.UpdateAPIView):
    pass


class PaymentDestroyAPIView(generics.DestroyAPIView):
    queryset = Payment.objects.all()
