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
    return render(request, "todolists/detail.html",
        {"task": task})

#This view allows user to create a new task
def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        completed = 'completed' in request.POST
        due_date = request.POST.get('due_date')

        task = Task(title=title, description=description, completed=completed, due_date=due_date)
        task.save()

        return render(request, "todolists/detail.html",
                      {"task": task})

    return render(request, "todolists/create.html")

#This view allows user to edit and update.html existing tasks
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

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST["choice"])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, "polls/detail.html", {
#             "question": question,
#             "error_message": "You didn't select a choice.",
#         },
#                       )
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#
#         return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})