from rest_framework import status
from rest_framework.test import APITestCase

from lms.models import Subscription, Course


class SubscriptionTestCase(APITestCase):

    def setUp(self) -> None:
        self.course = Course.objects.create(
            name='test course',
            description='test course description'
        )

        self.subscription = Subscription.objects.create(
            course=self.course,
            is_subscribed=True
        )

    def test_list(self):
        """Тест списка"""
        response = self.client.get(
            '/subscriptions/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            [{'id': self.subscription.id,
              'is_subscribed': self.subscription.is_subscribed,
              'course': self.course.pk,
              'owner': None}])

    def test_create(self):
        """Тест создания"""
        data = {
            "name": "test course",
            "description": "test course description",
            "course": self.course.pk
        }

        response = self.client.post(
            '/subscriptions/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Subscription.objects.all().count(), 2
        )
