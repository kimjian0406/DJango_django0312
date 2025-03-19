from django.urls import path
from .views import TodoCreateView, TodoUpdateView

urlpatterns = [
    path('create/', TodoCreateView.as_view(), name='todo_create'),
    path('<int:pk>/update/', TodoUpdateView.as_view(), name='todo_update'),
]

