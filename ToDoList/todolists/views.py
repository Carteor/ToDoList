from django.http import HttpResponse
from .models import Task
def index(request):
    task_list = Task.objects.all()
    output = ", ".join([t.title for t in task_list])
    return HttpResponse(output)

#This view displays detailed information about a specific task
def task_detail(request, task_id):
    response = "You are looking at the task %s."
    return HttpResponse(response % task_id)

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
