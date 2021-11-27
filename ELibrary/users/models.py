from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(verbose_name='Username', max_length=50, null=False, unique=True)
    email = models.EmailField(verbose_name='EMail', null=False, unique=True)
    info = models.TextField(verbose_name='Info', max_length=1000, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'