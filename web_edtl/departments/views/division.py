from django.shortcuts import render, redirect, get_object_or_404
from departments.models import  Division
from departments.forms import  DivisionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.utils import getnewid
from django.contrib import messages
from custom.decorators import allowed_users

@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def division_list(request):
    group = request.user.groups.all()[0].name
    objects = Division.objects.all().order_by('-datetime')
    context = {
        'title': 'Lista Divisaun', 'objects': objects, 'subtitle': 'Divisaun','group': group
    }
    return render(request, 'division/list.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def division_add(request):
    group = request.user.groups.all()[0].name
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
        'title': 'Aumenta Divisaun','subtitle': 'Divisaun', 'form': form,'group': group
    }
    return render(request, 'division/form.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def division_update(request, hashid):
    group = request.user.groups.all()[0].name
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
        'title': 'Altera Divisaun','subtitle': 'Divisaun', 'form': form,'group': group
    }
    return render(request, 'division/form.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def division_detail(request, hashid):
    group = request.user.groups.all()[0].name
    objects = get_object_or_404(Division, hashed=hashid)
    context = {
        'title': 'Detail Divisaun', 'subtitle': 'Division', 'objects': objects,'group': group
    }
    return render(request, 'division/detail.html', context)