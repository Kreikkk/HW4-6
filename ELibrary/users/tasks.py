import datetime

from celery import shared_task
from .models import User
from application.settings import BASE_DIR



@shared_task
def count_users():
    num_users = len(User.objects.filter(is_active=True))

    print(BASE_DIR)
    with open(f'{str(BASE_DIR)}/logs/users.log', 'a')as file:
        file.write(f'{datetime.datetime.now()}\t{num_users}\n')


@shared_task
def add(x, y):
    return BASE_DIR