from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Todo
from django.http import Http404
from django.db.models import Q

# Todo List View
class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = 'todo_cbv/todo_list.html'
    context_object_name = 'todos'
    paginate_by = 10  # 한 페이지에 10개씩 보여줌
    ordering = ['-created_at']  # 최근에 생성된 순서대로 정렬

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            queryset = Todo.objects.all()  # 관리자라면 모든 Todo를 볼 수 있음
        else:
            queryset = Todo.objects.filter(user=user)  # 일반 사용자는 자기 것만 보기
        search = self.request.GET.get('search', '')
        if search:
            queryset = queryset.filter(Q(title__icontains=search))  # 검색 기능 추가
        return queryset

# Todo Detail View
class TodoDetailView(LoginRequiredMixin, DetailView):
    model = Todo
    template_name = 'todo_cbv/todo_detail.html'

    def get_object(self):
        obj = super().get_object()
        if self.request.user != obj.user and not self.request.user.is_staff:
            raise Http404  # 권한이 없으면 404
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_dict'] = self.get_object().__dict__
        return context

# Todo Create View
class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    template_name = 'todo_cbv/todo_create.html'
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('cbv_todo_detail', kwargs={'pk': self.object.pk})

# Todo Update View
class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    template_name = 'todo_cbv/todo_update.html'
    fields = ['title', 'description']

    def get_object(self):
        obj = super().get_object()
        if self.request.user != obj.user and not self.request.user.is_staff:
            raise Http404  # 권한이 없으면 404
        return obj

    def get_success_url(self):
        return reverse_lazy('cbv_todo_detail', kwargs={'pk': self.object.pk})

# Todo Delete View
class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    template_name = 'todo_cbv/todo_confirm_delete.html'

    def get_object(self):
        obj = super().get_object()
        if self.request.user != obj.user and not self.request.user.is_staff:
            raise Http404  # 권한이 없으면 404
        return obj

    def get_success_url(self):
        return reverse_lazy('cbv_todo_list')

