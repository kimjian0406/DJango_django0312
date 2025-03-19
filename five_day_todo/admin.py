
from django.contrib import admin
from .models import Todo 

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'user')
    search_fields = ('title', 'user__username')
