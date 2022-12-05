from django.shortcuts import render, reverse
from rest_framework import viewsets
from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect

from s_chat.serializers import ChatGroupSerializer
from .models import ChatGroup, ChatGroupMessage

from a_user.models import Student

def chatindex(request):
    groups = ChatGroup.objects.all()
    return render(
        request,
        "chat.html",
        {"groups": groups}
    )

def user_login(request):
    students = Student.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 

        user = authenticate(username=username, password=password)
        if user in students:
            return HttpResponseRedirect(reverse('s_chat:chatindex'))
        else:
            return HttpResponse("Invalid username or password")
    else:
        return render(request, 'login.html', {})


def room(request, room_name):
    room = ChatGroup.objects.filter(name=room_name).first()
    chats = []

    if room:
        chats = ChatGroupMessage.objects.filter(group=room)
    else:
        room = ChatGroup(name=room_name)
        room.save()

    return render(request, 'room.html', {'room_name': room_name, 'chats': chats})

class ChatGroupViewSet(viewsets.ModelViewSet):
    serializer_class = ChatGroupSerializer
    queryset = ChatGroup.objects.all()


