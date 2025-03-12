from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm  # TodoForm은 우리가 만든 Form이야

# 할 일 생성
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user  # 현재 로그인한 유저를 Todo에 저장
            todo.save()
            return redirect('todo:todo_list')  # 할 일 목록 페이지로 리다이렉트
    else:
        form = TodoForm()
    return render(request, 'todo/todo_create.html', {'form': form})

# 할 일 수정
def todo_update(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo:todo_list')  # 할 일 목록 페이지로 리다이렉트
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_update.html', {'form': form, 'todo': todo})

# 할 일 삭제
def todo_delete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return redirect('todo:todo_list')  # 할 일 목록 페이지로 리다이렉트

