from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# rooms = [
#     {'id': 1, 'name': 'Lets play kahooti'},
#     {'id': 2, 'name': 'Lets edit videos'},
# ]


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    # can do in both ways
    # return render(request, 'home.html', {'rooms': rooms} )
    # the above way or by making context variable
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)

