from django.urls import path
from . import views

urlpatterns = [
    path('todo/<int:todo_id>/comments/', views.CommentListView.as_view(), name='comment_list'),
    path('todo/<int:todo_id>/comment/add/', views.CommentCreateView.as_view(), name='comment_create'),
    path('todo/comment/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment_edit'),
    path('todo/comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
]

