from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from .models import Todo
from .forms import CommentForm

class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todo_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        todo = self.object
        comments = todo.comments.all()  # 댓글 목록
        paginator = Paginator(comments, 5)  # 댓글 페이지네이션
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        context['comments'] = comments
        context['comment_form'] = CommentForm()
        context['page_obj'] = page_obj
        return context

