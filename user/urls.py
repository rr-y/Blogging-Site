from django.contrib import admin
from django.urls import path, include
from .views import register, profile


urlpatterns = [
    path('', register, name="register"),
    path('profile', profile, name="user-profile"),
]
