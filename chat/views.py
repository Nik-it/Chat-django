# chat/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MessageForm
from .models import Message

@login_required(login_url='login')
def chat(request):
    messages = Message.objects.all()
    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            Message.objects.create(sender=request.user, content=content)
            return redirect('chat')

    return render(request, 'chat/chat.html', {'messages': messages, 'form': form})

@login_required(login_url='login')
def clear_messages(request):
    if request.method == 'POST':
        Message.objects.all().delete()
    return redirect('chat')
