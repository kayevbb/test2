import os

from django.db import models
from django.urls import reverse
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

GENDER_CHOICES = [
    ['m', u"Крытай"],
    ['f', u"Не крытый"],
]

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='', blank=True, null=True, verbose_name='Фото')
    avatar1 = models.ImageField(upload_to='', verbose_name='Фото')
    avatar2 = models.ImageField(upload_to='', verbose_name='Фото')
    body = models.TextField(max_length=500, blank=True, null=True, verbose_name=u"Описание поля")
    address = models.CharField(max_length=60, blank=True, null=True, verbose_name=u'адрес')
    phone_number = models.CharField(max_length=14, blank=True, null=True, verbose_name='номер')
    city = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"Город")
    pole = models.CharField(max_length=10, verbose_name=u"Полe", choices=GENDER_CHOICES, default="m")
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse('home', args=[str(self.id)])