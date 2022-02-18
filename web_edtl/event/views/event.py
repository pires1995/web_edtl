from django.shortcuts import render, redirect, get_object_or_404
from event.models import Event
from event.forms import EventForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.utils import getnewid
from django.contrib import messages
from custom.decorators import allowed_users

@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def event_list(request):
    group = request.user.groups.all()[0].name
    objects = Event.objects.all()
    context = {
        'objects': objects, 'title': 'Lista Eventu',\
        'group': group, 
    }
    return render(request, 'event/list.html',context)

@login_required  
@allowed_users(allowed_roles=['admin','media'])
def event_add(request):
    group = request.user.groups.all()[0].name
    
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
        'title': 'Aumenta Eventu','subtitle': 'Eventu', 'form': form,'group': group,
        
    }
    return render(request, 'event/form.html', context)


@login_required
@allowed_users(allowed_roles=['admin','media'])
def event_update(request, hashid):
    group = request.user.groups.all()[0].name
    
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
        'title': 'Altera Evento','subtitle': 'Evento', 'form': form,'group': group,
        
    }
    return render(request, 'event/form.html', context)


@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def event_detail(request, hashid):
    group = request.user.groups.all()[0].name
    
    objects = get_object_or_404(Event, hashed=hashid)
    context = {
        'title': 'Detail Event', 'subtitle': 'Event', 'objects': objects,'group': group,
        
    }
    return render(request, 'event/detail.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def event_activate(request, hashid):
    group = request.user.groups.all()[0].name
    objects = get_object_or_404(Event, hashed=hashid)
    objects.is_active = True
    objects.save()
    messages.success(request, 'Successfully Activate Event')
    return redirect('admin-event-list')

@login_required
@allowed_users(allowed_roles=['admin','media'])
def event_deactivate(request, hashid):
    group = request.user.groups.all()[0].name
    objects = get_object_or_404(Event, hashed=hashid)
    objects.is_active = False
    objects.save()
    messages.success(request, 'Successfully Deactivate Event')
    return redirect('admin-event-list')