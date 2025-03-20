
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'), 
]
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
]
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('load-more-posts/', views.load_more_posts, name='load_more_posts'),
]
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    
]
urlpatterns = [
    path('tag/<str:tag_name>/', views.tag_posts, name='tag_posts'),
]
