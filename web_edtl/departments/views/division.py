from django.shortcuts import render, redirect, get_object_or_404
from departments.models import  Division
from departments.forms import  DivisionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from django.conf import settings
from main.utils import getnewid
from django.contrib import messages

@login_required
def division_list(request):
    objects = Division.objects.all().order_by('-datetime')
    context = {
        'title': 'Lista Divisaun', 'objects': objects, 'subtitle': 'Divisaun'
    }
    return render(request, 'division/list.html', context)

@login_required
def division_add(request):
    if request.method == 'POST':
        newid, new_hashed = getnewid(Division)
        form = DivisionForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id = newid
            instance.author = request.user
            instance.hashed = new_hashed
            instance.save()
            messages.success(request, f'Successfully Add Division')
            return redirect('admin-division-list')
    else:
        form = DivisionForm()
    context = {
        'title': 'Aumenta Divisaun','subtitle': 'Divisaun', 'form': form
    }
    return render(request, 'division/form.html', context)

@login_required
def division_update(request, hashid):
    objects = get_object_or_404(Division, hashed=hashid)
    if request.method == 'POST':    
        form = DivisionForm(request.POST, request.FILES, instance=objects)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, f'Successfully Update Division')
            return redirect('admin-division-list')
    else:
        form = DivisionForm(instance=objects)
    context = {
        'title': 'Altera Divisaun','subtitle': 'Divisaun', 'form': form
    }
    return render(request, 'division/form.html', context)

@login_required
def division_detail(request, hashid):
    objects = get_object_or_404(Division, hashed=hashid)
    context = {
        'title': 'Detail Divisaun', 'subtitle': 'Division', 'objects': objects
    }
    return render(request, 'division/detail.html', context)