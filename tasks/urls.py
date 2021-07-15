from django.urls import path
from tasks.views import list_task, create_task, edit_task, delete_task

app_name = 'tasks'

urlpatterns = [
    path('tasks', list_task, name='list_task'),
    path('tasks/create', create_task, name='create_task'),
    path('tasks/edit/<int:pk>', edit_task, name='edit_task'),
    path('tasks/delete/<int:pk>', delete_task, name='delete_task')
]