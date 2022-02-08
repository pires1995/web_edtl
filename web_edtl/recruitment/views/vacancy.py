from django.shortcuts import render, redirect, get_object_or_404
from recruitment.models import Vacancy
from recruitment.forms import VacancyForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from django.conf import settings
from main.utils import getnewid
from django.contrib import messages


@login_required
def vacancy_list(request):
    objects = Vacancy.objects.all().order_by('-datetime')
    context = {
        'objects': objects, 'title': 'Lista Internship',
    }
    return render(request, 'vacancy/list.html', context)

@login_required
def vacancy_add(request):
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
        'title': 'Aumenta Internship','subtitle': 'Internship', 'form': form
    }
    return render(request, 'vacancy/form.html', context)

@login_required
def vacancy_update(request, hashid):
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
        'title': 'Altera Departamento','subtitle': 'Departamento', 'form': form
    }
    return render(request, 'vacancy/form.html', context)

@login_required
def vacancy_detail(request, hashid):
    objects = get_object_or_404(Vacancy, hashed=hashid)
    context = {
        'title': 'Detail Vacancy', 'subtitle': 'Vacancy', 'objects': objects
    }
    return render(request, 'vacancy/detail.html', context)

@login_required
def vacancy_activate(request, hashid):
    objects = get_object_or_404(Vacancy, hashed=hashid)
    objects.is_active = True
    objects.save()
    messages.success(request, 'Successfully Activate Vacancy')
    return redirect('admin-vacancy-list')

@login_required
def vacancy_deactivate(request, hashid):
    objects = get_object_or_404(Vacancy, hashed=hashid)
    objects.is_active = False
    objects.save()
    messages.success(request, 'Successfully Deactivate Vacancy')
    return redirect('admin-vacancy-list')