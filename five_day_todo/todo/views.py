# todo/views.py
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from .models import Todo

class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todo/todo_info.html'
    context_object_name = 'todo'

    def get_object(self, queryset=None):
        todo = get_object_or_404(Todo, pk=self.kwargs['pk'])
        if not (self.request.user == todo.user or self.request.user.is_staff):
            raise Http404("You do not have permission to view this todo.")
        return todo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        todo = context['todo']
        context['username'] = todo.user.username
        return context

