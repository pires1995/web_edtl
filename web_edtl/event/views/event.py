from django.shortcuts import render, redirect, get_object_or_404
from event.models import Event
from event.forms import EventForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.utils import getnewid
from django.contrib import messages
from custom.decorators import allowed_users
from news.tasks import send_event,send_notification
from django.utils.text import Truncator
from news.models import NewsUser
import re
from custom.models import FirebaseToken
import requests
import json
from django.templatetags.static import static

image_url = static('main/img/logo.png')

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


def send_event_notification(registration_ids , message_title , message_desc, image):
    fcm_api = "AAAA79BRMps:APA91bFy0m7nCsQslCnlJQVFF3ubHfaVPy1lmrF-Hr2vUk-bOCdcZJLC7DR86T2LBz1ndVNC9eB6grmQOLg1RRMEB2V54MFtXCmrTVWd_953iS_Wc-Cdnf1dtALuCma1tCMVBxr6s8uk"
    url = "https://fcm.googleapis.com/fcm/send"
    
    headers = {
    "Content-Type":"application/json",
    "Authorization": 'key='+fcm_api}

    payload = {
        "registration_ids" :registration_ids,
        "priority" : "high",
        "notification" : {
            "body" : message_desc,
            "title" : f"News: {message_title}",
            "image" : image.url,
            "icon": image_url
            
        }
    }

    result = requests.post(url,  data=json.dumps(payload), headers=headers )
    print(result.json())

@login_required
@allowed_users(allowed_roles=['admin','media'])
def send_notif_user(request, hashid):
    token2 = FirebaseToken.objects.all()[0]
    token = [f'{token2}']
    print(token)
    objects = get_object_or_404(Event, hashed=hashid)
    objects.is_send_notif = True
    title = Truncator(objects.name_tet).words(5)
    send_notification(token, title, 'Test', objects.image)
    email_users = NewsUser.objects.filter(choices=1,is_active=True)
    for email_to in email_users:
        set_name = email_to.email
        set_name2 = re.split(r'[@.]', set_name)
        send_event.delay(email_to.email,set_name2[0], objects.name_tet)
    objects.save()
    messages.success(request, f'Successfully Send Notification')
    return redirect('admin-event-list')


