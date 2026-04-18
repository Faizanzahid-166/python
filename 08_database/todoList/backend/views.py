# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from django.http import HttpResponse

# 1. home view
def home(request):
    return render(request, "home.html")

 
# READ (List)
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/list.html', {'todos': todos})


# CREATE
def todo_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Todo.objects.create(title=title, description=description)
        return redirect('todo_list')
    return render(request, 'todo/create.html')


# UPDATE
def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.completed = 'completed' in request.POST
        todo.save()
        return redirect('todo_list')
    return render(request, 'todo/update.html', {'todo': todo})


# DELETE
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('todo_list')


def status(request):
    return HttpResponse("Todo App is Working 🚀")
