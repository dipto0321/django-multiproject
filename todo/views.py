from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem


def todoView(request):
    all_todos = TodoItem.objects.all()
    return render(request, 'index.html', {'todos': all_todos})


def todoadd(request):
    new_todo = TodoItem(content=request.POST['content'])
    new_todo.save()
    return HttpResponseRedirect('/todo')


def deletetodo(request, todo_id):
    item_del = TodoItem.objects.get(id=todo_id)
    item_del.delete()
    return HttpResponseRedirect('/todo')
