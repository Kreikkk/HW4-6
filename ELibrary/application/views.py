from django.views.decorators.http import require_GET
from django.shortcuts import render
from application.decorators import login_required


@login_required
@require_GET
def home(request):
    return render(request, 'home.html')


@require_GET
def login(request):
    return render(request, 'login.html')


@require_GET
def logout(request):
    return render(request, 'logout.html')


@require_GET
def info(request):
    return render(request, 'info.html')