from django.urls import path

from lms.apps import LmsConfig
from rest_framework.routers import DefaultRouter

from lms.views import lesson_views, payment_views, course_views, subscription_views

app_name = LmsConfig.name

router = DefaultRouter()
router.register(r'courses', course_views.CourseViewSet, basename='courses')
router.register(r'subscriptions', subscription_views.SubscriptionViewSet, basename='subscriptions')

urlpatterns = [
                  path('lessons/create/', lesson_views.LessonCreateAPIView.as_view(), name='lesson_create'),
                  path('lessons/', lesson_views.LessonListAPIView.as_view(), name='lessons_list'),
                  path('lessons/<int:pk>/', lesson_views.LessonRetrieveAPIView.as_view(), name='lesson'),
                  path('lessons/update/<int:pk>/', lesson_views.LessonUpdateAPIView.as_view(), name='lesson_update'),
                  path('lessons/delete/<int:pk>/', lesson_views.LessonDestroyAPIView.as_view(), name='lesson_delete'),

                  path('payments/create/', payment_views.PaymentCreateAPIView.as_view(), name='payment_create'),
                  path('payments/', payment_views.PaymentListAPIView.as_view(), name='payments_list'),
                  path('payments/<int:pk>/', payment_views.PaymentRetrieveAPIView.as_view(), name='payment'),
                  path('payments/update/<int:pk>/', payment_views.PaymentUpdateAPIView.as_view(),
                       name='payment_update'),
                  path('payments/delete/<int:pk>/', payment_views.PaymentDestroyAPIView.as_view(),
                       name='payment_delete'),

              ] + router.urls
