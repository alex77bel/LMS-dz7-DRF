from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import AccessToken

from lms.models import Course
from users.models import User


class CourseTestCase(APITestCase):

    def setUp(self) -> None:

        self.user = User.objects.create(
            email='user@test.test',
            password='12345',
            is_superuser=True,
            is_staff=True)
        self.client = APIClient()
        token = AccessToken.for_user(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        # self.client.force_authenticate(user=self.user)  # вариант

        self.course = Course.objects.create(
            name='test course',
            description='test course description',
            owner=self.user
        )

    def test_list(self):
        """Тест списка"""
        response = self.client.get(
            '/courses/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {'count': 1,
             'next': None,
             'previous': None,
             'results': [{'id': self.course.id,
                          'name': self.course.name,
                          'description': self.course.description,
                          'number_of_lessons': 0,
                          'lessons': [],
                          'owner': self.user.id,
                          'subscription': False}]})

    def test_create(self):
        """Тест создания"""
        data = {
            "name": "test course",
            "description": "test course description",
            "course": self.course.pk,
            "owner": 1
        }

        response = self.client.post(
            '/courses/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Course.objects.all().count(), 2
        )
