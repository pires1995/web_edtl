from django.shortcuts import render, redirect, get_object_or_404
from departments.models import Department
from departments.forms import DepartmentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.utils import getnewid, title_seo
from custom.decorators import allowed_users

@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def department_list(request):
    group = request.user.groups.all()[0].name
    objects = Department.objects.all()
    context = {
        'objects': objects, 'title': 'Lista Departamento',
        'group': group
    }
    return render(request, 'departments/list.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def department_add(request):
    group = request.user.groups.all()[0].name
    if request.method == 'POST':
        newid, new_hashed = getnewid(Department)
        form = DepartmentForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id = newid
            instance.title_seo = title_seo(form.cleaned_data.get('name_eng'))
            instance.author = request.user
            instance.hashed = new_hashed
            instance.save()
            messages.success(request, f'Successfully Add Department')
            return redirect('admin-department-list')
    else:
        form = DepartmentForm()
    context = {
        'title': 'Aumenta Departamento','subtitle': 'Departamento', 'form': form,
        'group': group
    }
    return render(request, 'departments/form.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def department_update(request, hashid):
    group = request.user.groups.all()[0].name
    objects = get_object_or_404(Department, hashed=hashid)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, request.FILES, instance=objects)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.title_seo = title_seo(form.cleaned_data.get('name_eng'))
            instance.author = request.user
            instance.save()
            messages.success(request, f'Successfully Update Department')
            return redirect('admin-department-list')
    else:
        form = DepartmentForm(instance=objects)
    context = {
        'title': 'Altera Departamento','subtitle': 'Departamento', 'form': form,
        'group': group
    }
    return render(request, 'departments/form.html', context)


@login_required
@allowed_users(allowed_roles=['admin','media', 'coordinator'])
def department_detail(request, hashid):
    group = request.user.groups.all()[0].name
    objects = get_object_or_404(Department, hashed=hashid)
    context = {
        'title': 'Detail Department', 'subtitle': 'Department', 'objects': objects,
        'group': group
    }
    return render(request, 'departments/detail.html', context)