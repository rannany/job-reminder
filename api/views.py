from rest_framework.response import Response
from rest_framework import viewsets, status, authentication, permissions
from django.shortcuts import get_object_or_404

from tasks.models import Task
from api.serializers import TaskSerializer


# Create your views here.

class TaskViewSet(viewsets.ViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        tasks = Task.objects.all()
        if request.query_params.get('done') or None:
            tasks = tasks.filter(is_done__exact=request.query_params.get('done') in ['True', 'true'] if True else False)
        if request.query_params.get('title') or None:
            tasks = tasks.filter(title__icontains=request.query_params.get('title'))
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def create(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'salvo com sucesso!'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
