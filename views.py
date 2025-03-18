from django.shortcuts import render
from .models import Todo
from .forms import TodoForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator

@login_required
def todo_list(request):
    query = request.GET.get('q', '')
    todos = Todo.objects.filter(user=request.user)
    
    if query:
        todos = todos.filter(Q(title__icontains=query) | Q(content__icontains=query))  # 검색 기능 구현

    paginator = Paginator(todos, 10)  # 한 페이지에 10개의 Todo
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'todo/todo_list.html', {'page_obj': page_obj, 'query': query})

