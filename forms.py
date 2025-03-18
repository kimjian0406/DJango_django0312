# todo/forms.py

from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'is_completed']

class TodoUpdateForm(TodoForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'is_completed']

