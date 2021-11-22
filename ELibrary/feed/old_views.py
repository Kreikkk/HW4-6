from django.http import response
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.views.decorators.http import require_GET, require_POST

from datetime import datetime
from random import choice, randint
from string import ascii_lowercase, digits


@require_GET
def feed(request, post_id):
    return JsonResponse({'post_id': post_id,
                         'title':   f'Post {post_id}',
                         'date_posted': str(datetime.now().year)})


@require_GET
def index(request):
    return render(request, 'index.html')


@require_POST
def create_post(request):
    return JsonResponse(request.POST)


@require_GET
def get_post_info(request):    
    title = ''.join(choice(ascii_lowercase + digits) for _ in range(10))
    response = {'post_id': randint(0, 1000),
                'title': title,
                'date_posted': f'{randint(2000, 2021)}'}

    return JsonResponse(response)


@require_GET
def get_list_of_posts(request):
    response = {}
    for i in range(3):
        title = ''.join(choice(ascii_lowercase + digits) for _ in range(10))
        response[i] = {'post_id': i,
                       'title': title,
                       'date_posted': f'{randint(2000, 2021)}'}

    return JsonResponse(response)