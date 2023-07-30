from rest_framework import serializers

from lms.models import Course, Lesson, Payment, Subscription
from lms.validators import VideoLinkValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [VideoLinkValidator(field='video_link')]  # валидация поля video_link


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    number_of_lessons = serializers.SerializerMethodField(read_only=True)
    lessons = LessonSerializer(source='lesson', many=True, read_only=True)  # список уроков в курсе
    subscription = serializers.SerializerMethodField(read_only=True)  # признак подписки

    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'number_of_lessons', 'lessons', 'owner', 'subscription')

    def get_number_of_lessons(self, instance): # возвращает количество уроков
        return instance.lesson.all().count()

    def get_subscription(self, instance): # возвращает признак подписки у текущего авторизованного пользователя
        auth_user = self.context['request'].user  # текущий авторизованный пользователь
        return Subscription.objects.filter(course=instance, owner=auth_user, is_subscribed=True).exists()


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
