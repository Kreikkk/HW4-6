from django.urls import path

from users.views import create_user, delete_user, get_user_info, update_user, get_list_of_users


urlpatterns = [
    path('create/', create_user, name='create_user'),
    path('delete/<str:email>/', delete_user, name='delete_user'),
    path('get_info/<str:email>/', get_user_info, name='get_user_info'),
    path('update/', update_user, name='update_user'),
    path('get_list/', get_list_of_users, name='get_list_of_users'),
]