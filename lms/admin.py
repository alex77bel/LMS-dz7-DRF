from django.contrib import admin

from lms.models import Course, Lesson, Payment, Subscription


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'owner', 'last_update')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'owner')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'owner', 'paid_at', 'paid_course', 'paid_lesson', 'payment_amount', 'payment_method', 'payment_id',
        'payment_status')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'owner', 'is_subscribed')
