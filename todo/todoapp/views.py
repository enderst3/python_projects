from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.template import loader

# Create your views here.

def index(request):
    task_list = Task.objects.all()
    # pass template to file
    context = {
        'task_list':task_list
    }
    return render(request, 'todoapp/index.html', context)

def detail(request, task_id):
    task = Task.objects.get(pk=task_id)
    context = {
        'task':task
    }
    return render(request, 'todoapp/detail.html', context)
