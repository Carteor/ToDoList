from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from .models import Task
from django.urls import reverse_lazy

class IndexView(generic.ListView):
    template_name = "todolists/index.html"
    context_object_name = "task_list"

    def get_queryset(self):
        return Task.objects.all()

class DetailView(generic.DetailView):
    model = Task
    template_name = "todolists/detail.html"

class CreateView(generic.CreateView):
    model = Task
    template_name = 'todolists/create.html'
    fields = ['title', 'description', 'completed', 'due_date']
    success_url = reverse_lazy('todolists:index')

#This view allows user to edit and update.html existing tasks
def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.completed = 'completed' in request.POST
        task.due_date = request.POST.get('due_date')

        task.save()

        return redirect('todolists:index')

    return render(request, 'todolists/update.html', {'task': task})

class UpdateView(generic.UpdateView):
    model = Task
    fields = ['title', 'description', 'completed', 'due_date']
    template_name = 'todolists/update.html'

    def get_success_url(self):
        return reverse_lazy('todolists:index')

class DeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy('todolists:index')
    template_name = 'todolists/confirm_delete.html'