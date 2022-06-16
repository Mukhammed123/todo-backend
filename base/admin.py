from django.contrib import admin
from .models import Todo, TodoList

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
  list_display = ["id", "title"]

class TodoItemAdmin(admin.ModelAdmin):
  list_display = ["id", "description", "finished", "todo_id"]

admin.site.register(Todo, TodoAdmin)
admin.site.register(TodoList, TodoItemAdmin)