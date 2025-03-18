# cbv_todo_app/models.py
from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.user.username}'  # 관리자에서 표시될 형식

    class Meta:
        ordering = ['-created_at']

