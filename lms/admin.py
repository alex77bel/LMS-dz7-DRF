from django.contrib import admin

from lms.models import Course, Lesson, Payment


@admin.register(Course)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

@admin.register(Lesson)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

@admin.register(Payment)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'paid_at', 'paid_course', 'paid_lesson', 'payment_amount', 'payment_method')

