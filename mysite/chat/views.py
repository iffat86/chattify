# chat/views.py
from django.shortcuts import render
from .models import signin

def index(request):
    if request.method == 'POST':
        form = signin()
        form.user_name = request.POST.get('username')
        form.user_email = request.POST.get('password')
        form.save()
 
    return render(request, 'index.html', {})

def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })