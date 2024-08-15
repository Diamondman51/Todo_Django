from django.shortcuts import get_object_or_404, redirect, render

from .models import Task


# Create your views here.
def tasks(req):
    not_completed = Task.objects.filter(is_completed=False).order_by('pk')
    completed = Task.objects.filter(is_completed=True).order_by('-pk')
    context = {
        'tasks': not_completed,
        'completed_tasks': completed
    }

    return render(req, 'home.html', context)


def addtask(req):
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    task = req.POST['task_name']
    Task.objects.create(task=task)
    return redirect('tasks')


def mark_as_done(req, pk):
    task = get_object_or_404(Task, id=pk)
    task.is_completed = True
    task.save()
    return redirect('tasks')


def delete_task(req, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('tasks')
