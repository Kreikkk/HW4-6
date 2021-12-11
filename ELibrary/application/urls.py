"""ELibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from application.views import home, info
from django.contrib.auth import views as auth_views

import posts.api.urls as post_urls
import users.api.urls as user_urls
from posts.api.views import PublisherDocumentView
from .views import fill_random_posts


urlpatterns = [
    path('', home, name='home'),
    path('info/', info, name='info'),
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('users/', include('users.urls')),
    path('search/', PublisherDocumentView.as_view({'get': 'list'})),
    path('fill_random_posts/', fill_random_posts, name='fill_random_posts'),
    \
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('social_auth/', include('social_django.urls', namespace='social')),
]

urlpatterns += post_urls.urlpatterns
urlpatterns += user_urls.urlpatterns
#Почему в root api показывается то, что тут первое?
