from django.shortcuts import render, redirect, get_object_or_404
from departments.models import Department, Division
from departments.forms import DepartmentForm, DivisionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from django.conf import settings
from main.utils import getnewid
from django.contrib import messages


@login_required
def department_list(request):
    objects = Department.objects.all()
    context = {
        'objects': objects, 'title': 'Lista Departamento',
    }
    return render(request, 'departments/list.html', context)

@login_required
def department_add(request):
    if request.method == 'POST':
        newid, new_hashed = getnewid(Department)
        form = DepartmentForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id = newid
            instance.author = request.user
            instance.hashed = new_hashed
            instance.save()
            messages.success(request, f'Successfully Add Department')
            return redirect('admin-department-list')
    else:
        form = DepartmentForm()
    context = {
        'title': 'Aumenta Departamento','subtitle': 'Departamento', 'form': form
    }
    return render(request, 'departments/form.html', context)

@login_required
def department_update(request, hashid):
    objects = get_object_or_404(Department, hashed=hashid)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, request.FILES, instance=objects)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, f'Successfully Update Department')
            return redirect('admin-department-list')
    else:
        form = DepartmentForm(instance=objects)
    context = {
        'title': 'Altera Departamento','subtitle': 'Departamento', 'form': form
    }
    return render(request, 'departments/form.html', context)


@login_required
def department_detail(request, hashid):
    objects = get_object_or_404(Department, hashed=hashid)
    context = {
        'title': 'Detail Department', 'subtitle': 'Department', 'objects': objects
    }
    return render(request, 'departments/detail.html', context)