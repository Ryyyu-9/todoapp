from django.shortcuts import render, redirect

from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def dashboard(request):
    tasks = Task.objects.order_by('deadline_date')
    context = {'tasks': tasks}
    return render(request, 'app/dashboard.html', context)

def task(request, task_id):
    task = Task.objects.get(id=task_id)
    task_detail = task.task_detail
    context = {'task': task, 'task_detail': task_detail}
    return render(request, 'app/detail_task.html', context)

def add_task(request):
    if request.method != 'POST':
        form = TaskForm()
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:dashboard')
    
    context = {'form': form}
    return render(request, 'app/add_task.html', context)