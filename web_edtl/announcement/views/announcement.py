from django.shortcuts import render, redirect, get_object_or_404
from announcement.models import Announcement
from announcement.forms import AnnoucementForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.utils import title_seo, getnewid
from custom.decorators import allowed_users
from news.tasks import send_announcement_notification, send_announcement
from django.utils.text import Truncator
from custom.models import FirebaseToken
from news.models import NewsUser
import re
# NEWS MANAGEMENT
@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def announcement_list(request):
    group = request.user.groups.all()[0].name
    objects = Announcement.objects.all().order_by('-datetime')
    context = {
        'news': objects, 'title': 'Announcement List', 'group': group
    }
    return render(request, 'announcement/list.html', context)


@login_required
@allowed_users(allowed_roles=['admin','media'])
def announcement_add(request):
    group = request.user.groups.all()[0].name
    if request.method == 'POST':
        newid, new_hashed = getnewid(Announcement)
        form = AnnoucementForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id = newid
            instance.author = request.user
            instance.hashed = new_hashed
            instance.save()
            messages.success(request, f'Successfully Add Announcement')
            return redirect('admin-announcement-list')
    else:
        form = AnnoucementForm()
    context = {
        'form': form, 'title': 'Add Announcement', 'group': group,
    }
    return render(request, 'announcement/form.html', context)


@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def announcement_detail(request, hashid):
    group = request.user.groups.all()[0].name
    objects = get_object_or_404(Announcement, hashed=hashid)
    context = {
        'objects': objects, 'title': 'News Detail',
        'group': group
    }
    return render(request, 'announcement/detail.html', context)


@login_required
@allowed_users(allowed_roles=['admin','media'])
def announcement_update(request, hashid):
    group = request.user.groups.all()[0].name
    object = get_object_or_404(Announcement, hashed=hashid)
    if request.method == 'POST':
        form = AnnoucementForm(request.POST, request.FILES, instance=object)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            if form.cleaned_data.get('title_tet') or form.cleaned_data.get('title_por') or form.cleaned_data.get('title_eng'):
                instance.title_seo = title_seo(form.cleaned_data.get('title_tet'))
            instance.save()
            messages.success(request, f'Successfully Update Announcement')
            return redirect('admin-announcement-list')
    else:
        form = AnnoucementForm(instance=object)
    context = {
        'form': form, 'title': 'Update Announcement', 'object': object, 'group': group,
    }
    return render(request, 'announcement/form.html', context)


@login_required
@allowed_users(allowed_roles=['admin','media'])
def announcement_activate(request, hashid):
    group = request.user.groups.all()[0].name
    object = get_object_or_404(Announcement, hashed=hashid)
    object.is_active = True
    object.save()
    messages.success(request, f'Successfully Activate Announcement')
    return redirect('admin-announcement-list')


@login_required
@allowed_users(allowed_roles=['admin','media'])
def announcement_deactivate(request, hashid):
    group = request.user.groups.all()[0].name
    object = get_object_or_404(Announcement, hashed=hashid)
    object.is_active = False
    object.save()
    messages.success(request, f'Successfully Deactivate Announcement')
    return redirect('admin-announcement-list')

@login_required
@allowed_users(allowed_roles=['admin','media'])
def announcement_send_notif(request, hashid):
    get_token = FirebaseToken.objects.all()[0]
    token = [f'{get_token}']
    objects = get_object_or_404(Announcement, hashed=hashid)
    objects.is_send_notif = True
    email_users = NewsUser.objects.filter(choices=3,is_active=True)
    for email_to in email_users:
        set_name = email_to.email
        set_name2 = re.split(r'[@.]', set_name)
        send_announcement.delay(email_to.email,set_name2[0], objects.title_tet)
    title = Truncator(objects.title_tet).words(5)
    headline = Truncator(objects.description_tet).words(5)
    send_announcement_notification(token, message_title=title, message_desc=headline, image=objects.image_thumbnail)
    objects.save()
    messages.success(request, f'Successfully Send Notifications')
    return redirect('admin-announcement-list')