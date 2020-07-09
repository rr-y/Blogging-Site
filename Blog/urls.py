
from django.contrib import admin
from django.urls import path, include
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, like_post, user_notify

urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('create/', PostCreateView.as_view(template_name="post_create.html"), name="post-create"),
    path('post/like/<int:id>/', like_post, name = 'like-post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name="blog-detail"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(template_name="post_update.html"), name="blog-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(template_name="post_delete.html"), name="blog-delete"),
    path('postnotification/<int:id>/', user_notify, name = "user-notify"),

]
