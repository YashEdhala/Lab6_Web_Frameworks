from django.shortcuts import render
from .models import Message


def home(request):
    return render(request, 'home.html')


def greet(request, name):
    return render(request, 'greet.html', {'name': name})


def message_list(request):
    messages = Message.objects.all()
    return render(
        request,
        'messages/message_list.html',
        {'messages': messages}
    )
