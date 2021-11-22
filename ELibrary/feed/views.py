from datetime import datetime
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from django.shortcuts import render

from users.models import User
from feed.models import Post, Category 


@require_POST
def create_post(request):
    dct = request.POST.dict()
    title = dct['title']
    category_name = dct['category']
    author_email = dct['author_email']
    body = dct['body']

    if None in (title, category_name, author_email, body):
        return HttpResponse(status=400)

    try:
        category = Category.objects.get(name=category_name)
        author = User.objects.get(email=author_email)
    except ObjectDoesNotExist:
        return HttpResponse(status=404)
    
    Post.objects.create(title=title, category=category, author=author, body=body)

    return JsonResponse({'created': dct})


@require_GET
def delete_post(request, idx):
    try:
        Post.objects.get(id=idx).delete()
    except ObjectDoesNotExist:
        return HttpResponse(status=404)

    return JsonResponse({'deleted': {'post_id': idx}})


@require_GET
def get_post_info(request, idx):
    try:
        post = Post.objects.get(id=idx)
    except ObjectDoesNotExist:
        return HttpResponse(status=404)

    info = {'id': idx,
            'title': post.title,
            'author': post.author.email,
            'pub_datetime': post.pub_datetime,
            'body': post.body,}

    return JsonResponse({'info': info})


@require_POST
def update_post(request):
    idx = request.POST.get('idx')
    title = request.POST.get('title')
    body = request.POST.get('body')
    Post.objects.filter(id=idx).update(title=title, body=body)

    try:
        post = Post.objects.get(id=idx)
    except ObjectDoesNotExist:
        return HttpResponse(status=404)

    info = {'idx': idx,
            'title': post.title,
            'author': post.author.email,
            'pub_datetime': post.pub_datetime,
            'body': post.body,}

    return JsonResponse({'updated': info})


@require_GET
def get_list_of_posts(request):
    posts = Post.objects.all()

    info = {post.id: {'title': post.title,
                      'author': post.author.email,
                      'pub_datetime': post.pub_datetime,
                      'body': post.body,} for post in posts}

    return JsonResponse({'info': info})

##########################################################################33

@require_GET
def feed(request, post_id):
    return JsonResponse({'post_id': post_id,
                         'title':   f'Post {post_id}',
                         'date_posted': str(datetime.now().year)})


@require_GET
def index(request):
    return render(request, 'index.html')




