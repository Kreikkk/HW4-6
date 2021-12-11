from django.views.decorators.http import require_GET
from django.shortcuts import render, redirect
from application.decorators import login_required
from posts.models import Post


def home(request):
    return render(request, 'home.html')


@login_required
def info(request):
    return render(request, 'info.html')


def fill_random_posts(request):
    ... 