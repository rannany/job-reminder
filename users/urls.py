from django.urls import path, include, re_path
from users.views import dashboard, register


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', dashboard, name='dashboard'),
    path('register', register, name='register'),
]
