# Generated by Django 4.2.3 on 2023-07-27 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0005_course_user_lesson_user_alter_payment_paid_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='course/', verbose_name='превью'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='course/', verbose_name='превью'),
        ),
    ]
