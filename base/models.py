from django.db import models

# Create your models here.
class Todo(models.Model):
  title = models.CharField(max_length=255)
  owner = models.ForeignKey('auth.User', related_name='todos', on_delete=models.CASCADE, default=None)

  class Meta:
    ordering = ['title']

  def __str__(self):
    return self.title

class TodoList(models.Model):
  description = models.TextField()
  finished = models.BooleanField()
  todo_id = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name="todo")

  class Meta:
    ordering = ['finished']

  def __str__(self):
    return self.description[0:30]