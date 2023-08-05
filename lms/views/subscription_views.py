
from rest_framework import viewsets

from config import settings

from lms.models import Subscription
from lms import serializers
from lms.views.lesson_views import SetOwnerMixin


class SubscriptionViewSet(SetOwnerMixin, viewsets.ModelViewSet):
    serializer_class = serializers.SubscriptionSerializer
    queryset = Subscription.objects.all()
