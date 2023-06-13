from django.contrib import admin
from django.urls import path, include
from .views import register_view, login_view, index


urlpatterns = [
    path('home/', index, name='home'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
]