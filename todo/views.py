from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoItem


def index(request):
    all_todos = TodoItem.objects.all()
    return render(request, 'index.html', {'todos': all_todos})
