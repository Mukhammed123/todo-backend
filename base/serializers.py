from rest_framework import serializers
from .models import TodoList
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Todo
    fields = ['id', 'title']

class TodoListSerializer(serializers.ModelSerializer):
  class Meta:
    model = TodoList
    fields = '__all__'

    read_only_field = ['todo_id']
