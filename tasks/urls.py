from django.urls import path
from tasks.views import create_task, edit_task, delete_task, TaskList

app_name = 'tasks'

urlpatterns = [
    path('tasks', TaskList.as_view(), name='list_task'),
    path('tasks/create', create_task, name='create_task'),
    path('tasks/edit/<int:pk>', edit_task, name='edit_task'),
    path('tasks/delete/<int:pk>', delete_task, name='delete_task')
]