from django.shortcuts import render, redirect, get_object_or_404
from tasks.models import Task
from django.urls import reverse
from tasks.forms import TaskForm


# Create your views here.


def list_task(request):
    context = {
        'tasks': Task.objects.all()
    }
    return render(request, 'tasks/list_tasks.html', context)


def create_task(request):
    if request.method == 'GET':
        context = {
            'form': TaskForm()
        }
        return render(request, 'tasks/create_task.html', context)
    elif request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('tasks:list_task'))


def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect(reverse('tasks:list_task'))
    return render(request, 'tasks/edit_task.html', {'form': form})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect(reverse('tasks:list_task'))
    return render(request, 'tasks/delete_confirm_task.html', context={'task': task})
