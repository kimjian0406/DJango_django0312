from django.shortcuts import render
from .models import Task

def task_list(request):
    tasks = Task.objects.all()  # Task 모델에서 모든 항목을 가져옴
    return render(request, 'task_list.html', {'tasks': tasks})
# todo/views.py
from django.shortcuts import render, redirect
from .forms import TaskForm

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # 목록 페이지로 리디렉션
    else:
        form = TaskForm()
    return render(request, 'task_create.html', {'form': form})

