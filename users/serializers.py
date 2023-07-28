from rest_framework import serializers

from lms.serializers import PaymentSerializer
from users.models import User


class UserSerializerAll(serializers.ModelSerializer):
    """Полный сериализатор"""
    payments = PaymentSerializer(source='payment', many=True)  # список платежей пользователя

    class Meta:
        model = User
        fields = ('id', 'email', 'phone', 'city', 'payments', 'is_superuser', 'is_staff', 'password')


class UserSerializerShort(serializers.ModelSerializer):
    """Сокращенный сериализатор, выводит часть данных"""

    class Meta:
        model = User
        fields = ('id', 'email', 'phone', 'city', 'is_superuser', 'is_staff')
