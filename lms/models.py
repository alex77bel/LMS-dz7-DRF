from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    description = models.CharField(max_length=255, verbose_name='описание')
    preview = models.ImageField(upload_to='course/', verbose_name='превью', null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ('name',)


class Lesson(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    description = models.CharField(max_length=255, verbose_name='описание')
    preview = models.ImageField(upload_to='course/', verbose_name='превью', null=True)
    video_link = models.URLField(verbose_name='ссылка на видео', null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ('name',)
