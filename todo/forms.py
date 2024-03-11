from django import forms

from .models import ToDoItem
from .models import Todo, Category, Priority


class ToDoItemForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ['title', 'description', 'priority']


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'completed', 'due_date', 'priority', 'categories']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class PriorityForm(forms.ModelForm):
    class Meta:
        model = Priority
        fields = ['name', 'level']
