from django.shortcuts import render, redirect
from .models import Task


def index(request):
    task_list = Task.objects.all()
    if request.method == "POST":
        name = request.POST.get("name", "")
        priority = request.POST.get("priority", "")

        task = Task(name=name, priority=priority)
        task.save()
        return redirect("/")

    return render(request, "my_app/index.html", {"task_list": task_list})
