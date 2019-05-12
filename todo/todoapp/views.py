from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('This is the todoapp homepage')

def detail(request):
    return HttpResponse('This is the detail view')
