from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin
from .models import Todo

class TodoAdmin(SummernoteModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'is_completed')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'start_date', 'end_date', 'is_completed', 'completed_image', 'thumbnail')
        }),
    )
    summernote_fields = ('description',)

admin.site.register(Todo, TodoAdmin)
