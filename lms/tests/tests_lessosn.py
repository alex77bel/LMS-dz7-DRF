from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import AccessToken

from lms.models import Lesson
from users.models import User


class LessonsTestCase(APITestCase):

    def setUp(self) -> None:

        self.user = User.objects.create(
            email='user@test.test',
            password='12345',
            is_superuser=True,
            is_staff=True)
        self.client = APIClient()
        token = AccessToken.for_user(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        self.lesson = Lesson.objects.create(
            name='test lesson',
            description='test lesson description',
            video_link='https://www.youtube.com/',
        )

    def test_list(self):
        """Тест списка"""
        response = self.client.get(
            reverse('lms:lessons_list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {"count": 1,
             "next": None,
             "previous": None,
             "results": [{"id": self.lesson.id,
                          "name": self.lesson.name,
                          "description": self.lesson.description,
                          "preview": None,
                          "video_link": self.lesson.video_link,
                          "course": None,
                          "owner": None}]})

    def test_create(self):
        """Тест создания"""
        data = {
            "name": "test lesson",
            "description": "test lesson description",
            "video_link": 'https://www.youtube.com/',
        }

        response = self.client.post(
            reverse('lms:lesson_create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Lesson.objects.all().count(), 2
        )

    def test_create_validation_error(self):
        """Тест валидации video_link"""
        data = {
            "name": "test lesson",
            "description": "test lesson description",
            "video_link": 'https://www.not_youtube.com/',
            # "owner": self.owner.pk
        }

        response = self.client.post(
            reverse('lms:lesson_create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            response.json(),
            {'video_link': ['Введите правильный URL.']}
        )
