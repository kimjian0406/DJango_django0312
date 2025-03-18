# cbv_todo_app/views.py
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Todo
from django.db.models import Q

# Todo ListView
class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = 'todo_list.html'
    context_object_name = 'todos'
    paginate_by = 10
    ordering = ['-created_at']
    
    def get_queryset(self):
        queryset = Todo.objects.all()
        # admin일 경우 모든 Todo를 조회, 일반 유저는 자신의 Todo만 조회
        if self.request.user.is_superuser:
            return queryset
        else:
            return queryset.filter(user=self.request.user)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        if query:
            context['todos'] = Todo.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        return context

# Todo DetailView
class TodoDetailView(LoginRequiredMixin, DetailView):
    model = Todo
    template_name = 'todo_info.html'
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not self.request.user.is_superuser and obj.user != self.request.user:
            raise Http404("You do not have permission to view this Todo.")
        return obj

# Todo CreateView
class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    template_name = 'todo_create.html'
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('cbv_todo_info', kwargs={'pk': self.object.pk})

# Todo UpdateView
class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    template_name = 'todo_update.html'
    fields = ['title', 'content']
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not self.request.user.is_superuser and obj.user != self.request.user:
            raise Http404("You do not have permission to edit this Todo.")
        return obj
    
    def get_success_url(self):
        return reverse_lazy('cbv_todo_info', kwargs={'pk': self.object.pk})

# Todo DeleteView
class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    template_name = 'todo_confirm_delete.html'
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not self.request.user.is_superuser and obj.user != self.request.user:
            raise Http404("You do not have permission to delete this Todo.")
        return obj
    
    def get_success_url(self):
        return reverse_lazy('cbv_todo_list')

