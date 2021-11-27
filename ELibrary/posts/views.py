from datetime import datetime
from django.db.models.query import RawQuerySet
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from django.shortcuts import render, get_object_or_404

from users.models import User
from posts.models import Post, Category 


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
def delete_post(request, pk):
    try:
        Post.objects.get(pk=pk).delete()
    except ObjectDoesNotExist:
        return HttpResponse(status=404)

    return JsonResponse({'deleted': {'post_id': pk}})


@require_GET
def get_post_info(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return HttpResponse(status=404)

    info = {'pk': pk,
            'title': post.title,
            'author': post.author.email,
            'pub_datetime': post.pub_datetime,
            'body': post.body,}

    return JsonResponse({'info': info})


@require_POST
def update_post(request):
    pk = request.POST.get('pk')
    title = request.POST.get('title')
    body = request.POST.get('body')
    Post.objects.filter(pk=pk).update(title=title, body=body)

    try:
        post = Post.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return HttpResponse(status=404)

    info = {'pk': pk,
            'title': post.title,
            'author': post.author.email,
            'pub_datetime': post.pub_datetime,
            'body': post.body,}

    return JsonResponse({'updated': info})


@require_GET
def get_list_of_posts(request):
    posts = Post.objects.all()

    info = {post.pk: {'title': post.title,
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




