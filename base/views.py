from cmath import nan
from .models import TodoList, Todo
from .serializers import TodoListSerializer, TodoSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Class based api views

class TodoView(APIView):

  def get(self, request, format=None):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)
  
  def post(self, request, format=None):
    data = request.data
    serializer = TodoSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

class TodoDetailView(APIView):

  def get_object(self, pk):
    try:
      return Todo.objects.get(id=pk)
    except:
      return Http404
  
  def get(self, request, pk, format=None):
    todoItem = self.get_object(pk)
    serializer = TodoSerializer(todoItem, many=False)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    todoItem = self.get_object(pk)
    data = request.data
    serializer = TodoSerializer(instance=todoItem, data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    print("Key: ", pk)
    todoItem = self.get_object(pk)
    todoItem.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class TodoItemsView(APIView):

  def get(self, request, format=None):
    todoItems = TodoList.objects.all()
    serializer = TodoListSerializer(todoItems, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    data = request.data
    serializer = TodoListSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

class TodoItemsDetailView(APIView):

  def get_todo_items(self, pk):
    try:
      return TodoList.objects.filter(todo_id=pk)
    except:
      return Http404
  
  def get_object(self, pk):
    try:
      return TodoList.objects.get(id=pk)
    except:
      return Http404

  def get(self, request, pk, format=None):
    todoItem = self.get_todo_items(pk)
    serializer = TodoListSerializer(todoItem, many=True)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    instance = self.get_object(pk)
    data = request.data
    serializer = TodoListSerializer(instance=instance, data=data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    todoItem = self.get_object(pk)
    todoItem.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)






# Functions based api views

# @api_view(["GET", "POST"])
# def todoView(request):
#   serializer = nan
#   data = request.data
#   if request.method == "GET":
#     todos = Todo.objects.all()
#     serializer = TodoSerializer(todos, many=True)
#   elif request.method == "POST":
#     serializer = TodoSerializer(data=data, many=False)
#     if serializer.is_valid():
#       serializer.save()
#   return Response(serializer.data)

# @api_view(["PUT", "DELETE"])
# def todoDetailView(request, pk):
#   instance = Todo.objects.get(id=pk)
#   data = request.data
#   if request.method == "DELETE":
#     instance.delete()
#     return Response({"message": "Todo was successfully deleted"})
#   elif request.method == "PUT":
#     serializer = TodoSerializer(instance=instance, data=data)
#     if serializer.is_valid():
#       serializer.save()
#     else:
#       return Response({"message": "Failed to Updated"})
#     return Response(serializer.data)

# @api_view(["GET", "POST"])
# def todoListView(request):
#   serializer = nan

#   if request.method == "POST":
#     serializer = TodoListSerializer(data=request.data, many=False)
#     if serializer.is_valid():
#       serializer.save()

#   elif request.method == "GET":
#     todoList = TodoList.objects.all()
#     serializer = TodoListSerializer(todoList, many=True)

#   return Response(serializer.data)

# @api_view(["GET", "PUT", "DELETE"])
# def todoListDetailView(request, pk):
#   print(request.method)
#   serializer = nan
#   if request.method == "PUT":
#     data = request.data
#     instance = TodoList.objects.get(id=pk)
#     serializer = TodoListSerializer(instance=instance, data=data)

#     if serializer.is_valid():
#       serializer.save()

#   elif request.method == "DELETE":
#     instance = TodoList.objects.get(id=pk)
#     instance.delete()
#     return Response({"message": "Todo item was successfully deleted"})
  
#   elif request.method == "GET":
#     todoList = TodoList.objects.filter(todo_id=pk)
#     serializer = TodoListSerializer(todoList, many=True)


#   return Response(serializer.data)
