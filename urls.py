from django.urls import path
from . import views

urlpatterns = [
    path('todo/create/', views.todo_create, name='todo_create'),
    path('todo/<int:todo_id>/update/', views.todo_update, name='todo_update'),
    path('todo/<int:todo_id>/delete/', views.todo_delete, name='todo_delete'),
]

