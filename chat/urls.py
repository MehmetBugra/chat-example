from django.urls import path
from .views import index


urlpatterns = [
    path('chat/<str:room_name>/', index, name='room'),
]