from django.views import generic
from django.shortcuts import render


def index(request, room_name=None):
    return render(request, 'index.html', {"room_name": room_name})