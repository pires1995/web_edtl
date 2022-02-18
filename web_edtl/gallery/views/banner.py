from django.shortcuts import render, redirect, get_object_or_404
from gallery.models import Banner
from gallery.forms import BannerForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from django.conf import settings
from main.utils import getnewid
from django.contrib import messages
from django.core.paginator import Paginator
from custom.decorators import allowed_users

@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def banner_list(request):
    group = request.user.groups.all()[0].name
    objects = Banner.objects.all().order_by('-datetime')
    paginator = Paginator(objects, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'objects': objects, 'page_obj': page_obj, \
        'title': 'Lista Banner', 'subtitle': 'Banner','group':group
    }
    return render(request, 'banner/list.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def banner_add(request):
	group = request.user.groups.all()[0].name
	if request.method == 'POST':
		newid, new_hashid = getnewid(Banner)
		form = BannerForm(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.id = newid
			instance.hashed = new_hashid
			instance.author = request.user
			instance.save()
			messages.success(request, f'Successfully add Banner')
			return redirect('admin-banner-list')
	else:
		form = BannerForm()
	context = {
		'form': form,
		'title': 'Add Banner', 'subtitle': 'Banner', 'group':group
	}
	return render(request, 'banner/form.html', context)


@login_required
@allowed_users(allowed_roles=['admin','media'])
def banner_update(request, hashid):
	group = request.user.groups.all()[0].name
	objects = get_object_or_404(Banner, hashed=hashid)
	if request.method == 'POST':
		form = BannerForm(request.POST, request.FILES, instance=objects)
		if form.is_valid():
			form.save()
			messages.success(request, f'Successfully update Banner')
			return redirect('admin-banner-list')
	else:
		form = BannerForm(instance=objects)
	context = {
		'hashid': hashid, 'objects': objects,'form': form,
		'title': 'Altera Banner', 'subtitle': 'Banner', 'group':group
	}
	return render(request, 'banner/form.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def banner_detail(request, hashid):
	group = request.user.groups.all()[0].name
	objects = get_object_or_404(Banner, hashed=hashid)
	context = {
		'title': 'Detalla Banner', 'group':group, 'objects': objects, 'banner': hashid 
	}
	return render(request, 'banner/detail.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def banner_activate(request, hashid):
    objects = get_object_or_404(Banner, hashed=hashid)
    objects.is_active = True
    objects.save()
    messages.success(request, 'Successfully Activate Banner')
    return redirect('admin-banner-list')

@login_required
@allowed_users(allowed_roles=['admin','media'])
def banner_deactivate(request, hashid):
    objects = get_object_or_404(Banner, hashed=hashid)
    objects.is_active = False
    objects.save()
    messages.success(request, 'Successfully Deactivate Banner')
    return redirect('admin-banner-list')