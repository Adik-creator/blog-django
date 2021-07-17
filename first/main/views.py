from django.shortcuts import render
from .models import Task


def index(request):
    tasks = Task.objects.order_by('-id')
    data = {
        'title': 'Главная сраница сайта',
        'values': ['hello', 'hi', 'whats app'],
        'tasks': tasks
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')