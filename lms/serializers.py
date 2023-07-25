from rest_framework import serializers

from lms.models import Course, Lesson, Payment


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    number_of_lessons = serializers.SerializerMethodField(read_only=True)
    lessons = LessonSerializer(source='lesson', many=True)  # список уроков в курсе

    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'number_of_lessons', 'lessons')

    def get_number_of_lessons(self, instance):
        return instance.lesson.all().count()  # количество уроков в курсе


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
