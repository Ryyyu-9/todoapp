from django.shortcuts import render

from .models import Task

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def dashboard(request):
    tasks = Task.objects.order_by('deadline_date')
    context = {'tasks': tasks}
    return render(request, 'app/dashboard.html', context)

