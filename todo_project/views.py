from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm, TodoUpdateForm

@login_required
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
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

