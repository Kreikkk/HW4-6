from django.urls import path, include
from posts.views import create_post, feed, get_list_of_posts, index, get_post_info, update_post, delete_post

urlpatterns = [
    path('post/<int:post_id>/', feed, name='feed'),
    path('index/', index, name='index'),
    \
    path('create/', create_post, name='create_post'),
    path('delete/<int:pk>/', delete_post, name='delete_post'),
    path('get_info/<int:pk>/', get_post_info, name='get_post_info'),
    path('update/', update_post, name='update_post'),
    path('post_list/', get_list_of_posts, name='get_list_of_posts'),
]
