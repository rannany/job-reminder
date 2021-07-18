from django.urls import path
from api.views import task_list

app_name = 'api'

urlpatterns =[
    path('tasks', task_list, name='tasks')
]