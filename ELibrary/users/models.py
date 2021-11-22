from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(verbose_name='Username', max_length=50)
    email = models.EmailField(verbose_name='EMail', null=False, unique=True)
    university = models.CharField(verbose_name='University', max_length=50, null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'