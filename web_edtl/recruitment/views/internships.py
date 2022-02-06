from django.shortcuts import render, redirect, get_object_or_404
from recruitment.models import Internships
from recruitment.forms import InternshipsForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from django.conf import settings
from main.utils import getnewid
from django.contrib import messages


@login_required
def internships_list(request):
    objects = Internships.objects.all().order_by('-datetime')
    context = {
        'objects': objects, 'title': 'Lista Vaga',
    }
    return render(request, 'internships/list.html', context)

@login_required
def internships_add(request):
    if request.method == 'POST':
        newid, new_hashed = getnewid(Internships)
        form = InternshipsForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id = newid
            instance.author = request.user
            instance.hashed = new_hashed
            instance.save()
            messages.success(request, f'Successfully Add Internships')
            return redirect('admin-internships-list')
    else:
        form = InternshipsForm()
    context = {
        'title': 'Aumenta Internship','subtitle': 'Internship', 'form': form
    }
    return render(request, 'internships/form.html', context)

@login_required
def internships_update(request, hashid):
    objects = get_object_or_404(Internships, hashed=hashid)
    if request.method == 'POST':
        form = InternshipsForm(request.POST, request.FILES, instance=objects)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, f'Successfully Update Internships')
            return redirect('admin-internships-list')
    else:
        form = InternshipsForm(instance=objects)
    context = {
        'title': 'Altera Internship','subtitle': 'Internship', 'form': form
    }
    return render(request, 'internships/form.html', context)

@login_required
def internships_detail(request, hashid):
    objects = get_object_or_404(Internships, hashed=hashid)
    context = {
        'title': 'Detail Internships', 'subtitle': 'Internships', 'objects': objects
    }
    return render(request, 'internships/detail.html', context)