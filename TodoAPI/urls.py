from django.urls import path
from .views import ToDoListCreateView, ToDoDetailView

urlpatterns = [
    path('todo/', ToDoListCreateView.as_view(), name='todo-list-create'),
    path('todo/<int:pk>/', ToDoDetailView.as_view(), name='todo-detail'),
]