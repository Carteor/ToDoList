from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render

from .models import Task

def index(request):
    task_list = Task.objects.all()
    context = {
        "task_list": task_list,
    }
    return render(request, "todolists/index.html", context)

#This view displays detailed information about a specific task
def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, "todolists/task_detail.html",
        {"task": task})

#This view allows user to create a new task
# def task_create(request):
#     return HttpResponse("You are creating a new task")

#This view allows user to edit and update existing tasks
def task_update(request, task_id):
    response = "You are updating task %s."
    return HttpResponse(response % task_id)

#This view allows to delete a specific task
def task_delete(request, task_id):
    response = "You are deleting task %s."
    return HttpResponse(response % task_id)

#This view toggles a specific task as complete or incomplete
# def task_complete(request, task_id):
#     response = "You are toggling task %s as in/complete."
#     return HttpResponse(response % task_id)
