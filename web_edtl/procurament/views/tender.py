from django.shortcuts import render, redirect, get_object_or_404
from procurament.models import Tender
from procurament.forms import TenderForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from django.conf import settings
from main.utils import getnewid
from django.contrib import messages
from custom.decorators import allowed_users

@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def tender_list(request):
    group = request.user.groups.all()[0].name
    objects = Tender.objects.all().order_by('-datetime')
    context = {
        'objects': objects, 'title': 'Lista Tender', 'group':group
    }
    return render(request, 'tender/list.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def tender_add(request):
    group = request.user.groups.all()[0].name
    if request.method == 'POST':
        newid, new_hashed = getnewid(Tender)
        form = TenderForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id = newid
            instance.author = request.user
            instance.hashed = new_hashed
            instance.save()
            messages.success(request, f'Successfully Add Tender')
            return redirect('admin-tender-list')
    else:
        form = TenderForm()
    context = {
        'title': 'Aumenta Tender', 'group':group, 'subtitle': 'Tender', 'form': form
    }
    return render(request, 'tender/form.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def tender_update(request, hashid):
    group = request.user.groups.all()[0].name
    objects = get_object_or_404(Tender, hashed=hashid)
    if request.method == 'POST':
        form = TenderForm(request.POST, request.FILES, instance=objects)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, f'Successfully Update Tender')
            return redirect('admin-tender-list')
    else:
        form = TenderForm(instance=objects)
    context = {
        'title': 'Altera Tender', 'group':group, 'subtitle': 'Tender', 'form': form
    }
    return render(request, 'tender/form.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def tender_detail(request, hashid):
    group = request.user.groups.all()[0].name
    objects = get_object_or_404(Tender, hashed=hashid)
    context = {
        'title': 'Detail Tender', 'group':group, 'subtitle': 'Tender', 'objects': objects
    }
    return render(request, 'tender/detail.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def tender_activate(request, hashid):
    objects = get_object_or_404(Tender, hashed=hashid)
    objects.is_active = True
    objects.save()
    messages.success(request, 'Successfully Activate Tender')
    return redirect('admin-tender-list')

@login_required
@allowed_users(allowed_roles=['admin','media'])
def tender_deactivate(request, hashid):
    objects = get_object_or_404(Tender, hashed=hashid)
    objects.is_active = False
    objects.save()
    messages.success(request, 'Successfully Deactivate Tender')
    return redirect('admin-tender-list')