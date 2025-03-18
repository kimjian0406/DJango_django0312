# todo/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Todo
from .forms import TodoForm, TodoUpdateForm

@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user)  # 로그인한 유저의 Todo만
    query = request.GET.get('q', '')
    if query:
        todos = todos.filter(Q(title__icontains=query) | Q(description__icontains=query))
    
    paginator = Paginator(todos, 10)  # 페이지네이션
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'todo/todo_list.html', {'page_obj': page_obj})

@login_required
def todo_info(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    return render(request, 'todo/todo_info.html', {'todo': todo})

@login_required
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user  # 로그인한 유저를 추가
            todo.save()
            return redirect('todo_info', todo_id=todo.id)
    else:
        form = TodoForm()
    return render(request, 'todo/todo_create.html', {'form': form})

@login_required
def todo_update(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    if request.method == 'POST':
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_info', todo_id=todo.id)
    else:
        form = TodoUpdateForm(instance=todo)
    return render(request, 'todo/todo_update.html', {'form': form})

@login_required
def todo_delete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.delete()
    return redirect('todo_list')

