from tkinter import CASCADE
from django.db import models

# Create your models here.
class Todo(models.Model):
  title = models.CharField(max_length=255)

  def __str__(self):
    return self.title

class TodoList(models.Model):
  description = models.TextField()
  finished = models.BooleanField()
  todo_id = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name="todo")

  def __str__(self):
    return self.description[0:30]