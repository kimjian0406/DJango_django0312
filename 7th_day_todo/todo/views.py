from django.shortcuts import render

from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from .models import Todo
from .forms import TodoForm, TodoUpdateForm
from django.urls import reverse_lazy

class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo/todo_create.html'
    success_url = reverse_lazy('todo_list') 

class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoUpdateForm
    template_name = 'todo/todo_update.html'
    success_url = reverse_lazy('todo_list') 

