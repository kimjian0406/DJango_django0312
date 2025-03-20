# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]

from django.urls import path
from .views import post_list, posts_by_tag

urlpatterns = [
    path('', post_list, name='post_list'),
    path('tag/<str:tag_name>/', posts_by_tag, name='posts_by_tag'), 
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('tag/<str:tag_name>/', views.posts_by_tag, name='posts_by_tag'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('tag/<str:tag_name>/', views.posts_by_tag, name='posts_by_tag'),
    path('search/', views.search_posts, name='search_posts'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('tag/<str:tag_name>/', views.posts_by_tag, name='posts_by_tag')
    path('search/', views.search_posts, name='search_posts'),
]
