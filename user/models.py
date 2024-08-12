from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    avatar = models.ImageField(upload_to='user/', blank=True, null=True, verbose_name='Фотография')
    about_me = models.TextField(blank=True, null=True, verbose_name='О себе',
                                default='Информация обо мне будет позже ... ')
    office = models.CharField(max_length=100, blank=True, null=True, verbose_name='Работа',
                              default='Работа будет добавлена позже')

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse(viewname='user:profile', kwargs={'user_id': self.pk})
