from django.shortcuts import render, redirect, get_object_or_404
from gallery.models import Album, Gallery
from gallery.forms import GalleryForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from django.conf import settings
from main.utils import getnewid
from django.contrib import messages
from django.core.paginator import Paginator
from custom.decorators import allowed_users

@login_required
@allowed_users(allowed_roles=['admin','media'])
def gallery_add(request, hashid):
    objects = get_object_or_404(Album, hashed=hashid)
    group = request.user.groups.all()[0].name
    if request.method == 'POST':
        data =request.POST
        image = request.FILES.getlist('image')
        for i in image:
            newid, new_hashid = getnewid(Gallery)
            object = Gallery.objects.create(
                id=newid,
                album=objects,
                overview_tet=data['overview_tet'],
                overview_por=data['overview_por'],
                overview_eng=data['overview_eng'],
                author=request.user,
                hashed=new_hashid,
                image=i
            )
        messages.success(request, f'Successfully add Image')
        return redirect('admin-album-list')
    else:
        form = GalleryForm()
    context = {
        'form': form, 'group':group,
        'title': f'Add One or More image to Album " {objects.name_tet} "  ', 'subtitle': 'Album'
    }
    return render(request, 'gallery/form.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def gallery_update(request, hashid):
    objects = get_object_or_404(Gallery, hashed=hashid)
    album = get_object_or_404(Album, hashed=objects.album.hashed)
    group = request.user.groups.all()[0].name
    if request.method == 'POST':
        form = GalleryForm(
            request.POST, request.FILES, instance=objects)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully Update Image')
            return redirect('admin-album-list')
    else:
        form = GalleryForm(instance=objects)
    context = {
        'form': form, 'group':group,
        'title': f'Add One or More image to Album " {album.name_tet} "  ', 'subtitle': 'Album'
    }
    return render(request, 'gallery/form.html', context)