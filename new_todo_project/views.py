from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Comment, Todo
from django.contrib.auth.mixins import LoginRequiredMixin

# 댓글 목록 페이지 (ListView)
class CommentListView(LoginRequiredMixin, ListView):
    model = Comment
    template_name = 'comments/comment_list.html'
    context_object_name = 'comments'
    
    def get_queryset(self):
        todo_id = self.kwargs['todo_id']
        todo = get_object_or_404(Todo, id=todo_id)
        return Comment.objects.filter(todo=todo)

# 댓글 작성 페이지 (CreateView)
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comments/comment_form.html'
    fields = ['message']
    
    def form_valid(self, form):
        todo = get_object_or_404(Todo, id=self.kwargs['todo_id'])
        form.instance.todo = todo
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        todo_id = self.kwargs['todo_id']
        return reverse('todo_detail', kwargs={'pk': todo_id})

# 댓글 수정 페이지 (UpdateView)
class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    template_name = 'comments/comment_form.html'
    fields = ['message']
    
    def get_success_url(self):
        todo_id = self.object.todo.id
        return reverse('todo_detail', kwargs={'pk': todo_id})

# 댓글 삭제 페이지 (DeleteView)
class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'comments/comment_confirm_delete.html'
    
    def get_success_url(self):
        todo_id = self.object.todo.id
        return reverse('todo_detail', kwargs={'pk': todo_id})

