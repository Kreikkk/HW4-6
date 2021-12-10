from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save
from django.dispatch import receiver
from celery import shared_task
from django.core.mail import send_mail

from application import local_settings


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


@shared_task
def inform_admin():
   send_mail('DB got updated', 'New user was created!', local_settings.EMAIL_HOST, local_settings.EMAIL_ADMIN_LIST)


@receiver(pre_save, sender=User)
def send_info_mail(sender, **kwargs):
    inform_admin.delay()