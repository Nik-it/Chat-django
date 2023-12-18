# chat/urls.py
from django.urls import path
from .views import chat, clear_messages

urlpatterns = [
    path('chat/', chat, name='chat'),
    path('clear-messages/', clear_messages, name='clear_messages'),
]
