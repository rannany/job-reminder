from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from tasks.models import Task
from django.urls import reverse
from tasks.forms import TaskForm


# Create your views here.


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(is_done=False).count()
        search_query = self.request.GET.get('search-query') or ''
        if search_query:
            context['tasks'] = context['tasks'].filter(title__icontains=search_query)
        context['search_input'] = search_query
        return context


@login_required()
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


@login_required()
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect(reverse('tasks:list_task'))
    return render(request, 'tasks/edit_task.html', {'form': form})


@login_required()
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect(reverse('tasks:list_task'))
    return render(request, 'tasks/delete_confirm_task.html', context={'task': task})
