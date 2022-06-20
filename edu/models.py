from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime


class User(AbstractUser):
    name = models.CharField(max_length=100, blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    is_teacher = models.BooleanField(default=False, blank=True)
    is_student = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name


class Razdel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название раздела')
    image = models.ImageField(upload_to='edu', verbose_name='Изображение')

    def __str__(self):
        return self.name


class Task(models.Model):
    razdel_id = models.ForeignKey(Razdel, on_delete=models.CASCADE, verbose_name='Разделы')
    is_to_send = models.BooleanField(default=False, verbose_name='Отправляемый')
    title = models.CharField(max_length=100, verbose_name='Название')
    file = models.FileField(upload_to='files/', verbose_name='Файл')

    def __str__(self):
        return self.title

    # class Meta:
    #     order_by = ('-id', )


class Homework(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    email = models.EmailField(max_length=150, blank=True, verbose_name='Email')
    description = models.TextField(verbose_name='Описание')
    file = models.FileField(verbose_name='Файл')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    taskid = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    occupation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='edu')

    def __str__(self):
        return self.name

