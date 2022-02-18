from django.shortcuts import render, redirect, get_object_or_404
from gallery.models import Video
from gallery.forms import VideoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from django.conf import settings
from main.utils import getnewid
from django.contrib import messages
from django.core.paginator import Paginator
from datetime import datetime
from custom.decorators import allowed_users

@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def video_list(request):
    group = request.user.groups.all()[0].name
    objects = Video.objects.all().order_by('-datetime')
    paginator = Paginator(objects, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'objects': objects, 'page_obj': page_obj, \
        'title': 'Lista Video', 'subtitle': 'Video', 'group':group
    }
    return render(request, 'video/list.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def video_add(request):
	group = request.user.groups.all()[0].name
	if request.method == 'POST':
		newid, new_hashid = getnewid(Video)
		form = VideoForm(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.id = newid
			instance.hashed = new_hashid
			instance.datetime = datetime.now()
			instance.author = request.user
			instance.save()
			messages.success(request, f'Successfully add Video')
			return redirect('admin-video-list')
	else:
		form = VideoForm()
	context = {
		'form': form,
		'title': 'Add Video', 'subtitle': 'Video', 'group':group
	}
	return render(request, 'video/form.html', context)


@login_required
@allowed_users(allowed_roles=['admin','media'])
def video_update(request, hashid):
	group = request.user.groups.all()[0].name
	objects = get_object_or_404(Video, hashed=hashid)
	if request.method == 'POST':
		form = VideoForm(request.POST, request.FILES, instance=objects)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.datetime = datetime.now()
			instance.save()
			messages.success(request, f'Successfully update Video')
			return redirect('admin-video-list')
	else:
		form = VideoForm(instance=objects)
	context = {
		'hashid': hashid, 'objects': objects,'form': form,
		'title': 'Altera Video', 'subtitle': 'Video', 'group':group
	}
	return render(request, 'video/form.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def video_detail(request, hashid):
	group = request.user.groups.all()[0].name
	objects = get_object_or_404(Video, hashed=hashid)
	context = {
		'title': 'Detalla Video', 'objects': objects,'group':group, 'video': hashid 
	}
	return render(request, 'video/detail.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def video_activate(request, hashid):
    objects = get_object_or_404(Video, hashed=hashid)
    objects.is_active = True
    objects.save()
    messages.success(request, 'Successfully Activate Video')
    return redirect('admin-video-list')

@login_required
@allowed_users(allowed_roles=['admin','media'])
def video_deactivate(request, hashid):
    objects = get_object_or_404(Video, hashed=hashid)
    objects.is_active = False
    objects.save()
    messages.success(request, 'Successfully Deactivate Video')
    return redirect('admin-video-list')