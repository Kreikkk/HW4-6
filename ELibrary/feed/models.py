from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import PROTECT
from django.utils.timezone import now

from users.models import User


# Create your models here.
class Category(Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, to_field='name',on_delete=PROTECT)
    author = models.ForeignKey(User, to_field='email', on_delete=PROTECT)
    pub_datetime = models.DateTimeField(default=now)
    body = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'