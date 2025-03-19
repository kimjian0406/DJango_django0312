from django.shortcuts import render

django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Todo, Comment
from .forms import CommentForm
from django.core.paginator import Paginator

class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todo/todo_info.html'
    context_object_name = 'todo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        # 댓글을 페이지네이션
        comments = Comment.objects.filter(todo=self.object).order_by('-created_at')
        paginator = Paginator(comments, 5)  # 페이지당 5개 댓글
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'todo/comment_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.todo = get_object_or_404(Todo, pk=self.kwargs['todo_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('cbv_todo_detail', kwargs={'pk': self.object.todo.pk})

class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'todo/comment_form.html'

    def get_object(self):
        comment = super().get_object()
        if comment.user != self.request.user and not self.request.user.is_staff:
            raise PermissionError("You do not have permission to edit this comment.")
        return comment

    def get_success_url(self):
        return reverse_lazy('cbv_todo_detail', kwargs={'pk': self.object.todo.pk})

class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'todo/comment_confirm_delete.html'

    def get_object(self):
        comment = super().get_object()
        if comment.user != self.request.user and not self.request.user.is_staff:
            raise PermissionError("You do not have permission to delete this comment.")
        return comment

    def get_success_url(self):
        return reverse_lazy('cbv_todo_detail', kwargs={'pk': self.object.todo.pk})
