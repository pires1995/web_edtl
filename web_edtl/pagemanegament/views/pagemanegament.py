from django.shortcuts import render, redirect, get_object_or_404
from pagemanegament.models import PageManegament
from pagemanegament.forms import PageManegamentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from django.conf import settings
from main.utils import getnewid
from django.contrib import messages
from custom.decorators import allowed_users

@login_required
@allowed_users(allowed_roles=['admin','media'])
def pagemanegament_list(request):
    group = request.user.groups.all()[0].name
    objects = PageManegament.objects.all()
    context = {
        'objects': objects, 'title': 'Lista FAQ','group':group
    }
    return render(request, 'pagemanegament/list.html',context)


@login_required
@allowed_users(allowed_roles=['admin','media'])
def pagemanegament_add(request):
    group = request.user.groups.all()[0].name
    if request.method == 'POST':
        newid, new_hashed = getnewid(PageManegament)
        form = PageManegamentForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id = newid
            instance.author = request.user
            instance.hashed = new_hashed
            instance.save()
            messages.success(request, f'Successfully Add PageManegament')
            return redirect('admin-pagemanegament-list')
    else:
        form = PageManegamentForm()
    context = {
        'title': 'Aumenta PageManegament', 'group':group, 'subtitle': 'PageManegament', 'form': form
    }
    return render(request, 'pagemanegament/form.html', context)


@login_required
@allowed_users(allowed_roles=['admin','media'])
def pagemanegament_update(request, hashid):
    group = request.user.groups.all()[0].name
    objects = get_object_or_404(PageManegament, hashed=hashid)
    if request.method == 'POST':
        form = PageManegamentForm(request.POST, request.FILES, instance=objects)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, f'Successfully Update PageManegament')
            return redirect('admin-pagemanegament-list')
    else:
        form = PageManegamentForm(instance=objects)
    context = {
        'title': 'Altera PageManegamento', 'group':group, 'subtitle': 'PageManegamento', 'form': form
    }
    return render(request, 'pagemanegament/form.html', context)


@login_required
@allowed_users(allowed_roles=['admin','media'])
def pagemanegament_detail(request, hashid):
    group = request.user.groups.all()[0].name
    objects = get_object_or_404(PageManegament, hashed=hashid)
    context = {
        'title': 'Detail PageManegament', 'group':group, 'subtitle': 'PageManegament', 'objects': objects
    }
    return render(request, 'pagemanegament/detail.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def pagemanegament_activate(request, hashid):
    objects = get_object_or_404(PageManegament, hashed=hashid)
    objects.is_active = True
    objects.save()
    messages.success(request, 'Successfully Activate PageManegament')
    return redirect('admin-pagemanegament-list')

@login_required
@allowed_users(allowed_roles=['admin','media'])
def pagemanegament_deactivate(request, hashid):
    objects = get_object_or_404(PageManegament, hashed=hashid)
    objects.is_active = False
    objects.save()
    messages.success(request, 'Successfully Deactivate PageManegament')
    return redirect('admin-pagemanegament-list')