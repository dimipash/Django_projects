from django.shortcuts import render

from .models import ChatRoom


def index(request):
    chat_rooms = ChatRoom.objects.all()
    return render(request, "chat_app/index.html", {"chat_rooms": chat_rooms})


def chat_room(request, slug):
    chat_room = ChatRoom.objects.get(slug=slug)
    return render(request, "chat_app/room.html", {"chat_room": chat_room})
