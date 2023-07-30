from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from lms.models import Course


class CourseTestCase(APITestCase):

    def setUp(self) -> None:
        self.course = Course.objects.create(
            name='test course',
            description='test course description',
            owner=None
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
                          'preview': None,
                          'owner': None}]})

    def test_create(self):
        """Тест создания"""
        data = {
            "name": "test course",
            "description": "test course description",
            "course": self.course.pk
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
