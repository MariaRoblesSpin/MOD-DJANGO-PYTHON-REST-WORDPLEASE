"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

from posts.api import PostsAPI, PostDetailAPI
from posts.views import post_detail, new_post, LatestPostsView, PostsListView, BlogsListView, UserPostsView
from users.api import UserDetailAPI, UserAPI
from users.views import login, logout, SignUpFormView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Users
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('signup', SignUpFormView.as_view(), name='signup'),

    # posts
    path('blogs/<str:name>/<int:pk>/', post_detail, name='post_detail'),
    path('blogs/<str:name>/', UserPostsView.as_view(), name='blog_user'),
    path('all_posts', PostsListView.as_view(), name='post_list'),
    path('post/new/', new_post, name='new_post'),

    # blogs
    path('blogs', BlogsListView.as_view(), name='blogs'),

    # home
    path('', LatestPostsView.as_view(), name='home'),

    # API
    path('api/posts/<int:pk>', PostDetailAPI.as_view(), name='post_detail_api'),
    path('api/posts/<str:name>', PostsAPI.as_view(), name='posts_api'),

    path('api/users/<int:pk>', UserDetailAPI.as_view(), name='user_detail_api'),
    path('api/users', UserAPI.as_view(), name='posts_api')


]

