from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='test@test.ru',
        )

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
              'is_superuser': False,
              'is_staff': False}])

    def test_create(self):
        """Тест создания"""
        data = {
            "email": 'test1@test.ru',
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
