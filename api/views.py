from tasks.models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import TaskSerializer


# Create your views here.

@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all()
    if request.query_params.get('done') or None:
        tasks = tasks.filter(is_done__exact=request.query_params.get('done') in ['True', 'true'] if True else False)
    if request.query_params.get('title') or None:
        tasks = tasks.filter(title__icontains=request.query_params.get('title'))
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)
