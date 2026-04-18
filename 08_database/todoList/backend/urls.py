from django.urls import path
from . import views

urlpatterns = [
    path('todo/list/', views.todo_list, name='todo_list'),
    path('todo/create/', views.todo_create, name='todo_create'),
    path('todo/update/<int:pk>/', views.todo_update, name='todo_update'),
    path('todo/delete/<int:pk>/', views.todo_delete, name='todo_delete'),
    path('todo/status/', views.status, name='status'),
    path('', views.home, name='home'),
]


