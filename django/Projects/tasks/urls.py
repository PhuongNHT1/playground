from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.list_tasks, name='tasks'),
    path('add_task/', views.add_task, name='add_task')
]