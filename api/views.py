from rest_framework.response import Response
from rest_framework import viewsets, status, authentication, permissions
from django.shortcuts import get_object_or_404

from tasks.models import Task
from api.serializers import TaskSerializer


# Create your views here.

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# class TaskViewSet(viewsets.ViewSet):
#     authentication_classes = [authentication.TokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated, IsOwner]
#
#     def list(self, request):
#         tasks = Task.objects.filter(user=request.user)
#         if request.query_params.get('done') or None:
#             tasks = tasks.filter(is_done__exact=request.query_params.get('done') in ['True', 'true'] if True else False)
#         if request.query_params.get('title') or None:
#             tasks = tasks.filter(title__icontains=request.query_params.get('title'))
#         serializer = TaskSerializer(tasks, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         task = get_object_or_404(Task, pk=pk)
#         serializer = TaskSerializer(task)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'status': 'salvo com sucesso!'})
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
