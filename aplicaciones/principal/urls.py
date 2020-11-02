from django.urls import path 
from . import views
from .models import Post
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('post/new/',),
]