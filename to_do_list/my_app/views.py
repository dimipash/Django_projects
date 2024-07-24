from django.shortcuts import render, redirect
from .models import Task
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy


class TaskListView(ListView):
    model = Task
    template_name = 'my_app/index.html'
    context_object_name = 'task_list'


class TaskDetailView(DetailView):
    model = Task
    template_name ='my_app/detail.html'
    context_object_name = 'task'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'my_app/update.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('cbv-detail', kwargs={'pk':self.object.id})
    
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'my_app/delete.html'
    success_url = reverse_lazy('cbv-index')


def index(request):
    task_list = Task.objects.all()
    if request.method == "POST":
        name = request.POST.get("name", "")
        priority = request.POST.get("priority", "")
        date = request.POST.get("date", "")
        task = Task(name=name, priority=priority, date=date)
        task.save()
        return redirect("/")

    return render(request, "my_app/index.html", {"task_list": task_list})

def delete(request, task_id):
    task = Task.objects.get(id=task_id)     
    if request.method == "POST":
        task.delete()
        return redirect("/")
    
    return render(request, "my_app/delete.html", {"task": task})

def update(request, id):
    task = Task.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, "my_app/edit.html", {"form": form, 'task': task})