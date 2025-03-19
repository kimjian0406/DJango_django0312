# todo/urls.py
# todo/urls.py
urlpatterns = [
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:task_id>/update/', views.task_update, name='task_update'),
]

# todo/urls.py
urlpatterns = [
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:task_id>/update/', views.task_update, name='task_update'),
    path('tasks/<int:task_id>/delete/', views.task_delete, name='task_delete'),
]

from django.urls import path
from .views import TodoListView, TodoDetailView, TodoCreateView, TodoUpdateView, TodoDeleteView

urlpatterns = [
    path('', TodoListView.as_view(), name='cbv_todo_list'),  # Todo 리스트 페이지
    path('create/', TodoCreateView.as_view(), name='cbv_todo_create'),  # Todo 생성 페이지
    path('<int:pk>/', TodoDetailView.as_view(), name='cbv_todo_detail'),  # Todo 상세 페이지
    path('<int:pk>/update/', TodoUpdateView.as_view(), name='cbv_todo_update'),  # Todo 수정 페이지
    path('<int:pk>/delete/', TodoDeleteView.as_view(), name='cbv_todo_delete'),  # Todo 삭제 페이지
]

from django.urls import path
from .views import TodoListView, TodoDetailView, TodoCreateView, TodoUpdateView, TodoDeleteView

urlpatterns = [
    path('', TodoListView.as_view(), name='cbv_todo_list'),
    path('create/', TodoCreateView.as_view(), name='cbv_todo_create'),
    path('<int:pk>/', TodoDetailView.as_view(), name='cbv_todo_detail'),
    path('<int:pk>/update/', TodoUpdateView.as_view(), name='cbv_todo_update'),
    path('<int:pk>/delete/', TodoDeleteView.as_view(), name='cbv_todo_delete'),
]

