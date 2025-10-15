from django.views import generic
from django.shortcuts import render
from .models import Message


def index(request, room_name=None):
    messages = Message.objects.filter(room_name=room_name).order_by('timestamp')[:50]
    return render(request, 'index.html', {"room_name": room_name, "messages": messages})