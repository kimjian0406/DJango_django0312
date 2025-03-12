from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    # 할 일 생성
    path('create/', views.todo_create, name='todo_create'),
    
    # 할 일 수정
    path('<int:todo_id>/update/', views.todo_update, name='todo_update'),
    
    # 할 일 삭제
    path('<int:todo_id>/delete/', views.todo_delete, name='todo_delete'),
]

