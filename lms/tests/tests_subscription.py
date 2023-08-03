from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import AccessToken

from lms.models import Subscription, Course
from users.models import User


class SubscriptionTestCase(APITestCase):

    def setUp(self) -> None:

        self.user = User.objects.create(
            email='user@test.test',
            password='12345',
            is_superuser=True,
            is_staff=True)
        self.client = APIClient()
        token = AccessToken.for_user(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')


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
