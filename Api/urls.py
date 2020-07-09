from django.contrib import admin
from django.urls import path, include
import django.contrib.auth.views as auth_view
from django.conf import settings
from django.conf.urls.static import static
from .views import api_detail_blog_view, PostDetail, PostList

urlpatterns = [
    path('postlist/', PostList.as_view(), name = 'list'),
    path('postdetail/<int:pk>/', PostDetail.as_view(), name = 'detail'),
]

