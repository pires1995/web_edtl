from django.shortcuts import render, redirect, get_object_or_404
from recruitment.models import Vacancy
from recruitment.forms import VacancyForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.utils import getnewid
from django.contrib import messages
from custom.decorators import allowed_users

@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def vacancy_list(request):
    group = request.user.groups.all()[0].name
    objects = Vacancy.objects.all().order_by('-datetime')
    context = {
        'objects': objects,'group': group, 'title': 'Lista Internship',
    }
    return render(request, 'vacancy/list.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def vacancy_add(request):
    group = request.user.groups.all()[0].name
    if request.method == 'POST':
        newid, new_hashed = getnewid(Vacancy)
        form = VacancyForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id = newid
            instance.author = request.user
            instance.hashed = new_hashed
            instance.save()
            messages.success(request, f'Successfully Add Vacancy')
            return redirect('admin-vacancy-list')
    else:
        form = VacancyForm()
    context = {
        'title': 'Aumenta Internship','group': group,'subtitle': 'Internship', 'form': form
    }
    return render(request, 'vacancy/form.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def vacancy_update(request, hashid):
    group = request.user.groups.all()[0].name
    objects = get_object_or_404(Vacancy, hashed=hashid)
    if request.method == 'POST':
        form = VacancyForm(request.POST, request.FILES, instance=objects)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, f'Successfully Update Vacancy')
            return redirect('admin-vacancy-list')
    else:
        form = VacancyForm(instance=objects)
    context = {
        'title': 'Altera Departamento','group': group,'subtitle': 'Departamento', 'form': form
    }
    return render(request, 'vacancy/form.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def vacancy_detail(request, hashid):
    group = request.user.groups.all()[0].name
    objects = get_object_or_404(Vacancy, hashed=hashid)
    context = {
        'title': 'Detail Vacancy','group': group, 'subtitle': 'Vacancy', 'objects': objects
    }
    return render(request, 'vacancy/detail.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def vacancy_activate(request, hashid):
    objects = get_object_or_404(Vacancy, hashed=hashid)
    objects.is_active = True
    objects.save()
    messages.success(request, 'Successfully Activate Vacancy')
    return redirect('admin-vacancy-list')

@login_required
@allowed_users(allowed_roles=['admin','media'])
def vacancy_deactivate(request, hashid):
    objects = get_object_or_404(Vacancy, hashed=hashid)
    objects.is_active = False
    objects.save()
    messages.success(request, 'Successfully Deactivate Vacancy')
    return redirect('admin-vacancy-list')