from django.http import HttpResponse
from django.shortcuts import render


def hello_world(request):
    return render(request, "hello-world.html", {})


def health_check(request):
    return HttpResponse("OK", status=200)
