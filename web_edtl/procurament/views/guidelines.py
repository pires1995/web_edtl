from django.shortcuts import render, redirect, get_object_or_404
from procurament.models import Guidelines
from procurament.forms import GuidelinesForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from django.conf import settings
from main.utils import getnewid
from django.contrib import messages


@login_required
def guidelines_list(request):
    objects = Guidelines.objects.all().order_by('-datetime')
    context = {
        'objects': objects, 'title': 'Lista Guidelines',
    }
    return render(request, 'guidelines/list.html', context)

@login_required
def guidelines_add(request):
    if request.method == 'POST':
        newid, new_hashed = getnewid(Guidelines)
        form = GuidelinesForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id = newid
            instance.author = request.user
            instance.hashed = new_hashed
            instance.save()
            messages.success(request, f'Successfully Add Guidelines')
            return redirect('admin-guidelines-list')
    else:
        form = GuidelinesForm()
    context = {
        'title': 'Aumenta Guidelines','subtitle': 'Guidelines', 'form': form
    }
    return render(request, 'guidelines/form.html', context)

@login_required
def guidelines_update(request, hashid):
    objects = get_object_or_404(Guidelines, hashed=hashid)
    if request.method == 'POST':
        form = GuidelinesForm(request.POST, request.FILES, instance=objects)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, f'Successfully Update Guidelines')
            return redirect('admin-guidelines-list')
    else:
        form = GuidelinesForm(instance=objects)
    context = {
        'title': 'Altera Guidelines','subtitle': 'Guidelines', 'form': form
    }
    return render(request, 'guidelines/form.html', context)

@login_required
def guidelines_detail(request, hashid):
    objects = get_object_or_404(Guidelines, hashed=hashid)
    context = {
        'title': 'Detail Guidelines', 'subtitle': 'Guidelines', 'objects': objects
    }
    return render(request, 'guidelines/detail.html', context)

@login_required
def guidelines_activate(request, hashid):
    objects = get_object_or_404(Guidelines, hashed=hashid)
    objects.is_active = True
    objects.save()
    messages.success(request, 'Successfully Activate Guidelines')
    return redirect('admin-guidelines-list')

@login_required
def guidelines_deactivate(request, hashid):
    objects = get_object_or_404(Guidelines, hashed=hashid)
    objects.is_active = False
    objects.save()
    messages.success(request, 'Successfully Deactivate Guidelines')
    return redirect('admin-guidelines-list')