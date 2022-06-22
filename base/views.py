from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from .forms import RoomForm
from .models import Room, Topic

# rooms = [
#     {'id': 1, 'name': 'Lets play kahooti'},
#     {'id': 2, 'name': 'Lets edit videos'},
# ]


def home(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''

# THIS WHOLE BELOW CODE IS FOR SEARCH FUNCTIONALITY

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )
    # | symbol stands for (or) in django

    topics = Topic.objects.all()

    # this count method runs faster than python len function

    room_count = rooms.count()
    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count}
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


def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
#add primary key to know which iem we are going to update
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
             form.save()
        return redirect('home')


    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})