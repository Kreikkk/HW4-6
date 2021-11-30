from django.core.checks.messages import Info
from django.views.decorators.http import require_GET, require_POST
from django.http import HttpResponse, JsonResponse
from users.models import User
from django.shortcuts import get_object_or_404, render

from application.decorators import login_required


def login(request):
    return render(request, 'login.html')


@login_required
def home(request):
    return render(request, 'home.html')


@require_POST
def create_user(request):
    dct = request.POST.dict()
    username = dct['username']
    email = dct['email']
    university = dct['university']

    if None in (username, email, university):
        return HttpResponse(status=400)

    User.objects.create(username=username, email=email, university=university)

    return JsonResponse({'create': dct})


@require_GET
def delete_user(request, email):
    user = get_object_or_404(User, email=email)
    user.delete()

    return JsonResponse({'deleted': {'user_email': email}})


@require_GET
def get_user_info(request, email):
    user = get_object_or_404(User, email=email)
  
    info = {'email': user.email,
            'username': user.username,
            'university': user.university,}

    return JsonResponse({'info': info})


@require_POST
def update_user(request):
    email = request.POST.get('email')
    username = request.POST.get('username')
    university = request.POST.get('university')
    
    User.objects.filter(email=email).update(username=username, university=university)
    user = get_object_or_404(User, email=email)

    info = {'email': email,
            'username': username,
            'university': university}

    return JsonResponse({'updated': info})


@require_GET
def get_list_of_users(request):
    users = User.objects.all()

    data = {user.email: {'username': user.username, 
                         'university': user.university,} for user in users}

    return JsonResponse({'info': data})
