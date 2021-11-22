from django.core.checks.messages import Info
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST
from django.http import HttpResponse, JsonResponse
from users.models import User
from  django.core.exceptions import ObjectDoesNotExist
# Create your views here.


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
    try:
        User.objects.get(email=email).delete()
    except ObjectDoesNotExist:
        return HttpResponse(status=404)

    return JsonResponse({'deleted': {'user_email': email}})


@require_GET
def get_user_info(request, email):
    try:
        user = User.objects.get(email=email)
    except ObjectDoesNotExist:
        return HttpResponse(status=404)

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

    try:
        post = User.objects.get(email=email)
    except ObjectDoesNotExist:
        return HttpResponse(status=404)

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
