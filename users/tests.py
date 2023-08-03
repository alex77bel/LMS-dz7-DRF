from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import AccessToken

from users.models import User


class UserTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='user@test.test',
            password='12345',
            is_superuser=True,
            is_staff=True)
        self.client = APIClient()
        token = AccessToken.for_user(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_list(self):
        """Тест списка"""
        response = self.client.get(
            '/users/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [{'id': self.user.pk,
              'email': self.user.email,
              'phone': None,
              'city': None,
              'is_superuser': True,
              'is_staff': True,
              }])

    def test_create(self):
        """Тест создания"""
        data = {
            'email': 'user1@test.test'
        }

        response = self.client.post(
            '/users/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            User.objects.all().count(), 2
        )
