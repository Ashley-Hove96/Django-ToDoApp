from django.urls import path

from . import views

urlpatterns = [
    # URLs for Todo
    path('', views.todo_list, name='todo_list'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('delete_todo/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('todo/<int:pk>/edit/', views.edit_todo, name='edit_todo'),

    # URLs for Category
    path('category/', views.category_list, name='category_list'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<int:pk>/edit/', views.edit_category, name='edit_category'),
    path('category/<int:pk>/delete/', views.delete_category, name='delete_category'),

    # URLs for Priority
    path('priority/', views.priority_list, name='priority_list'),
    path('add_priority/', views.add_priority, name='add_priority'),
]
