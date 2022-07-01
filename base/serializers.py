from rest_framework import serializers
from .models import TodoList
from .models import Todo
from user.serializers import UserSerializer

class TodoSerializer(serializers.ModelSerializer):
  # owner = serializers.ReadOnlyField(source='owner.username')
  def get_num_tasks(self, obj):
    return obj.todo.filter(finished=False).count()
    
  owner = UserSerializer(read_only=True)
  num_tasks = serializers.SerializerMethodField()
  class Meta:
    model = Todo
    fields = [
      'id',
      'title',
      'owner',
      'num_tasks'
    ]


class CreateTodoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Todo
    fields = [
      'title',
      'owner'
    ]

class TodoListSerializer(serializers.ModelSerializer):
  class Meta:
    model = TodoList
    fields = '__all__'

    read_only_field = ['todo_id']
