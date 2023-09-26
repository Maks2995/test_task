from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Training(models.Model):
    name = models.CharField(max_length=128)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Lesson(models.Model):
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    name = models.CharField(max_length=123)
    desc = models.CharField(max_length=255)
    link = models.URLField(verbose_name=None)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
