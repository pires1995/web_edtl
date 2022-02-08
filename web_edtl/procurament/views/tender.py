from django.shortcuts import render, redirect, get_object_or_404
from procurament.models import Tender
from procurament.forms import TenderForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from django.conf import settings
from main.utils import getnewid
from django.contrib import messages


@login_required
def tender_list(request):
    objects = Tender.objects.all().order_by('-datetime')
    context = {
        'objects': objects, 'title': 'Lista Tender',
    }
    return render(request, 'tender/list.html', context)

@login_required
def tender_add(request):
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
        'title': 'Aumenta Tender','subtitle': 'Tender', 'form': form
    }
    return render(request, 'tender/form.html', context)

@login_required
def tender_update(request, hashid):
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
        'title': 'Altera Tender','subtitle': 'Tender', 'form': form
    }
    return render(request, 'tender/form.html', context)

@login_required
def tender_detail(request, hashid):
    objects = get_object_or_404(Tender, hashed=hashid)
    context = {
        'title': 'Detail Tender', 'subtitle': 'Tender', 'objects': objects
    }
    return render(request, 'tender/detail.html', context)

@login_required
def tender_activate(request, hashid):
    objects = get_object_or_404(Tender, hashed=hashid)
    objects.is_active = True
    objects.save()
    messages.success(request, 'Successfully Activate Tender')
    return redirect('admin-tender-list')

@login_required
def tender_deactivate(request, hashid):
    objects = get_object_or_404(Tender, hashed=hashid)
    objects.is_active = False
    objects.save()
    messages.success(request, 'Successfully Deactivate Tender')
    return redirect('admin-tender-list')