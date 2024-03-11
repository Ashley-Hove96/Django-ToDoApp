from django.db import models


# Create your models here.

class ToDoItem(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title





class Todo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    priority = models.ForeignKey('Priority', on_delete=models.CASCADE)
    categories = models.ManyToManyField('Category')
    due_date = models.DateField()

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Priority(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=0)

    def __str__(self):
        return self.name

