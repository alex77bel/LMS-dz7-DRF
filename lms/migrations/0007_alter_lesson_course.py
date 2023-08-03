# Generated by Django 4.2.3 on 2023-07-27 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0006_alter_course_preview_alter_lesson_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lesson', to='lms.course', verbose_name='курс'),
        ),
    ]
