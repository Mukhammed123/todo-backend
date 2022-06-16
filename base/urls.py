from django.urls import path
from . import views

urlpatterns = [
  path('list/<str:pk>/', views.TodoItemsDetailView.as_view()),
  path('list/', views.TodoItemsView.as_view()),
  path('<str:pk>/', views.TodoDetailView.as_view()),
  path('', views.TodoView.as_view()),
]