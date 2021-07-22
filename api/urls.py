from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from api.views import TaskViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, 'task')
urlpatterns = [
    path('', include(router.urls), name='tasks'),
    path('login', obtain_auth_token, name='login')
]
