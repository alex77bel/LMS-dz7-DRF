from rest_framework import serializers

from lms.serializers import PaymentSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(source='payment', many=True)  # список платежей пользователя

    class Meta:
        model = User
        fields = ('id', 'email', 'phone', 'city', 'payments')
