from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import ToDo

# Create your views here.
def home(request):
    todo_items = ToDo.objects.all().order_by('-added_date')
    return render(request, 'todo_app/index.html', {
        'todo_items': todo_items
    })


def add_todo(request):
    text = request.POST.get('todotext')
    ToDo.objects.create(text=text)
    return HttpResponseRedirect('/')


def delete_todo(request, todo_id):
    ToDo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')
