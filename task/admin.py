from django.contrib import admin

from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'task', 'is_completed', 'created_at', 'updated_at']
    search_fields = ['task']
    list_filter = ['is_completed']
    ordering = ['id']
    list_editable = ['task', 'is_completed']


# Register your models here.
admin.site.register(Task, TaskAdmin)