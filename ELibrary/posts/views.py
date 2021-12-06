from datetime import datetime
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.http import require_GET, require_POST
from datetime import datetime
from django.shortcuts import get_object_or_404
from application.decorators import login_required

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

    author = get_object_or_404(User, email=author_email)
    category = get_object_or_404(Category, name=category_name)

    Post.objects.create(title=title, category=category, author=author, body=body)

    return JsonResponse({'created': dct})


@login_required
@require_GET
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if post.author.username != request.user.username:
        return HttpResponse(status=404)

    post.delete()
    return JsonResponse({'deleted': {'post_id': pk}})


@login_required
@require_GET
def get_post_info(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.author.username != request.user.username:
        return HttpResponse(status=404)

    info = {'pk': pk,
            'title': post.title,
            'author': post.author.username,
            'pub_datetime': post.pub_datetime,
            'body': post.body,}

    return JsonResponse({'info': info})


@require_POST
def update_post(request):
    pk = request.POST.get('pk')
    title = request.POST.get('title')
    body = request.POST.get('body')
    Post.objects.filter(pk=pk).update(title=title, body=body)
    post = get_object_or_404(Post, pk=pk)

    info = {'pk': pk,
            'title': post.title,
            'author': post.author.email,
            'pub_datetime': post.pub_datetime,
            'body': post.body,}

    return JsonResponse({'updated': info})


@login_required
@require_GET
def get_list_of_posts(request):
    posts = Post.objects.filter(author = request.user)


    info = {post.pk: {'title': post.title,
                      'author': post.author.username,
                      'author_email': post.author.email,
                      'pub_datetime': post.pub_datetime,
                      'body': post.body,} for post in posts}

    return JsonResponse({'info': info})
