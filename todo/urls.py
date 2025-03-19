
from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.TodoDetailView.as_view(), name='cbv_todo_detail'),
    path('comment/<int:todo_id>/create/', views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
]

