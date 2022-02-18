from django.shortcuts import render, redirect, get_object_or_404
from gallery.models import Album, Gallery
from gallery.forms import AlbumForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from main.utils import getnewid
from django.contrib import messages
from django.core.paginator import Paginator
from datetime import datetime
from custom.decorators import allowed_users

@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def album_list(request):
    group = request.user.groups.all()[0].name
    objects = Album.objects.all().order_by('-datetime')
    paginator = Paginator(objects, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'objects': objects, 'page_obj': page_obj, \
        'title': 'Lista Album', 'subtitle': 'Album', 'group': group
    }
    return render(request, 'album/list.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def album_add(request):
	group = request.user.groups.all()[0].name
	if request.method == 'POST':
		newid, new_hashid = getnewid(Album)
		form = AlbumForm(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.id = newid
			instance.hashed = new_hashid
			instance.datetime = datetime.now()
			instance.author = request.user
			instance.save()
			messages.success(request, f'Successfully add Album')
			return redirect('admin-album-list')
	else:
		form = AlbumForm()
	context = {
		'form': form,
		'title': 'Add Album', 'subtitle': 'Album', 'group':group
	}
	return render(request, 'album/form.html', context)


@login_required
@allowed_users(allowed_roles=['admin','media'])
def album_update(request, hashid):
	group = request.user.groups.all()[0].name
	objects = get_object_or_404(Album, hashed=hashid)
	if request.method == 'POST':
		form = AlbumForm(request.POST, request.FILES, instance=objects)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.datetime = datetime.now()
			instance.save()
			messages.success(request, f'Successfully update Album')
			return redirect('admin-album-list')
	else:
		form = AlbumForm(instance=objects)
	context = {
		'hashid': hashid, 'objects': objects,'form': form,
		'title': 'Altera Album', 'subtitle': 'Album', 'group':group
	}
	return render(request, 'album/form.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def album_detail(request, hashid):
	group = request.user.groups.all()[0].name
	gallery = None
	try:
		objects = get_object_or_404(Album, hashed=hashid)
		gallery = Gallery.objects.filter(album=objects)
	except:
		objects = get_object_or_404(Album, hashed=hashid)
	context = {
		'title': 'Detalla Album', 'group': group, 'objects': objects, 'album': hashid , 'gallery': gallery
	}
	return render(request, 'album/detail.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def album_activate(request, hashid):
    objects = get_object_or_404(Album, hashed=hashid)
    objects.is_active = True
    objects.save()
    messages.success(request, 'Successfully Activate Album')
    return redirect('admin-album-list')

@login_required
@allowed_users(allowed_roles=['admin','media'])
def album_deactivate(request, hashid):
    objects = get_object_or_404(Album, hashed=hashid)
    objects.is_active = False
    objects.save()
    messages.success(request, 'Successfully Deactivate Album')
    return redirect('admin-album-list')