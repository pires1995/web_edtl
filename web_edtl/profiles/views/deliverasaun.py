from django.shortcuts import render, redirect, get_object_or_404
from profiles.models import Deliverasaun
from profiles.forms import DeliverasaunForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.utils import getnewid
from django.contrib import messages
from custom.decorators import allowed_users


@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def deliverasaun_list(request):
    group = request.user.groups.all()[0].name
    objects = Deliverasaun.objects.all().order_by('-datetime')
    context = {
        'objects': objects,'group': group, 'title': 'Lista Deliverasaun',
    }
    return render(request, 'deliverasaun/list.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def deliverasaun_add(request):
    group = request.user.groups.all()[0].name
    if request.method == 'POST':
        newid, new_hashed = getnewid(Deliverasaun)
        form = DeliverasaunForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id = newid
            instance.author = request.user
            instance.hashed = new_hashed
            instance.save()
            messages.success(request, f'Successfully Add Deliverasaun')
            return redirect('admin-deliverasaun-list')
    else:
        form = DeliverasaunForm()
    context = {
        'title': 'Aumenta Deliverasaun','group': group,'subtitle': 'Deliverasaun', 'form': form
    }
    return render(request, 'deliverasaun/form.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def deliverasaun_update(request, hashid):
    group = request.user.groups.all()[0].name
    objects = get_object_or_404(Deliverasaun, hashed=hashid)
    if request.method == 'POST':
        form = DeliverasaunForm(request.POST, request.FILES, instance=objects)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, f'Successfully Update Deliverasaun')
            return redirect('admin-deliverasaun-list')
    else:
        form = DeliverasaunForm(instance=objects)
    context = {
        'title': 'Altera Deliverasaun','group': group,'subtitle': 'Deliverasaun', 'form': form
    }
    return render(request, 'deliverasaun/form.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def deliverasaun_detail(request, hashid):
    group = request.user.groups.all()[0].name
    objects = get_object_or_404(Deliverasaun, hashed=hashid)
    context = {
        'title': 'Detail Deliverasaun','group': group, 'subtitle': 'Deliverasaun', 'objects': objects
    }
    return render(request, 'deliverasaun/detail.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def deliverasaun_activate(request, hashid):
    objects = get_object_or_404(Deliverasaun, hashed=hashid)
    objects.is_active = True
    objects.save()
    messages.success(request, 'Successfully Activate Deliverasaun')
    return redirect('admin-deliverasaun-list')

@login_required
@allowed_users(allowed_roles=['admin','media'])
def deliverasaun_deactivate(request, hashid):
    objects = get_object_or_404(Deliverasaun, hashed=hashid)
    objects.is_active = False
    objects.save()
    messages.success(request, 'Successfully Deactivate Deliverasaun')
    return redirect('admin-deliverasaun-list')