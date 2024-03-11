from django.shortcuts import render, redirect, get_object_or_404

from .forms import TodoForm, CategoryForm, PriorityForm, ToDoItemForm
from .models import Todo, Category, Priority, ToDoItem


def todo_list(request):
    todo = Todo.objects.all()
    return render(request, 'todo/todo_list.html', {'todo': todo})


def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo/add_todo.html', {'form': form})


def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todo/delete_todo.html', {'todo': todo})


def edit_todo(request, pk):
    todo_item = ToDoItem.objects.get(pk=pk)
    if request.method == 'POST':
        form = ToDoItemForm(request.POST, instance=todo_item)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = ToDoItemForm(instance=todo_item)
    return render(request, 'todo/edit_todo.html', {'form': form})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'todo/category_list.html', {'categories': categories})


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'todo/add_category.html', {'form': form})


def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'todo/edit_category.html', {'form': form})


def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'todo/delete_category.html', {'category': category})


def priority_list(request):
    priorities = Priority.objects.all()
    return render(request, 'todo/priority_list.html', {'priorities': priorities})


def add_priority(request):
    if request.method == 'POST':
        form = PriorityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('priority_list')
    else:
        form = PriorityForm()
    return render(request, 'todo/add_priority.html', {'form': form})
