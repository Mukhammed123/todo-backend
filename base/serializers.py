from rest_framework import serializers
from .models import TodoList
from .models import Todo
from user.serializers import UserSerializer

class TodoSerializer(serializers.ModelSerializer):
  # owner = serializers.ReadOnlyField(source='owner.username')
  owner = UserSerializer(read_only=True)
  class Meta:
    model = Todo
    fields = [
      'id',
      'title',
      'owner'
    ]

class TodoListSerializer(serializers.ModelSerializer):
  class Meta:
    model = TodoList
    fields = '__all__'

    read_only_field = ['todo_id']
