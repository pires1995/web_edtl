from django.shortcuts import render, redirect, get_object_or_404
from event.models import Event
from event.forms import EventForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from django.conf import settings
from main.utils import getnewid
from django.contrib import messages


@login_required
def event_list(request):
    objects = Event.objects.all()
    context = {
        'objects': objects, 'title': 'Lista Eventu'
    }
    return render(request, 'event/list.html',context)

def event_add(request):
    if request.method == 'POST':
        newid, new_hashed = getnewid(Event)
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id = newid
            instance.author = request.user
            instance.hashed = new_hashed
            instance.save()
            messages.success(request, f'Successfully Add Event')
            return redirect('admin-event-list')
    else:
        form = EventForm()
    context = {
        'title': 'Aumenta Eventu','subtitle': 'Eventu', 'form': form
    }
    return render(request, 'event/form.html', context)


@login_required
def event_update(request, hashid):
    objects = get_object_or_404(Event, hashed=hashid)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=objects)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, f'Successfully Update Event')
            return redirect('admin-event-list')
    else:
        form = EventForm(instance=objects)
    context = {
        'title': 'Altera Evento','subtitle': 'Evento', 'form': form
    }
    return render(request, 'event/form.html', context)


@login_required
def event_detail(request, hashid):
    objects = get_object_or_404(Event, hashed=hashid)
    context = {
        'title': 'Detail Event', 'subtitle': 'Event', 'objects': objects
    }
    return render(request, 'event/detail.html', context)

@login_required
def event_activate(request, hashid):
    objects = get_object_or_404(Event, hashed=hashid)
    objects.is_active = True
    objects.save()
    messages.success(request, 'Successfully Activate Event')
    return redirect('admin-event-list')

@login_required
def event_deactivate(request, hashid):
    objects = get_object_or_404(Event, hashed=hashid)
    objects.is_active = False
    objects.save()
    messages.success(request, 'Successfully Deactivate Event')
    return redirect('admin-event-list')