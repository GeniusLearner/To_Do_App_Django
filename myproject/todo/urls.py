from django.contrib import admin
from django.urls import path, include
from todo import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('delete_todo/<int:todo_id>/', views.delete_todo, name="delete_todo"),
]
