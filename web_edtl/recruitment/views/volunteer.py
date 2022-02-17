from django.shortcuts import render, redirect, get_object_or_404
from recruitment.models import Volunteer
from recruitment.forms import VolunteerForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from django.conf import settings
from main.utils import getnewid
from django.contrib import messages


@login_required
def volunteer_list(request):
    objects = Volunteer.objects.all().order_by('-datetime')
    context = {
        'objects': objects, 'title': 'Lista Vaga',
    }
    return render(request, 'volunteer/list.html', context)

@login_required
def volunteer_add(request):
    if request.method == 'POST':
        newid, new_hashed = getnewid(Volunteer)
        form = VolunteerForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id = newid
            instance.author = request.user
            instance.hashed = new_hashed
            instance.save()
            messages.success(request, f'Successfully Add Volunteer')
            return redirect('admin-volunteer-list')
    else:
        form = VolunteerForm()
    context = {
        'title': 'Aumenta Internship','subtitle': 'Internship', 'form': form
    }
    return render(request, 'volunteer/form.html', context)

@login_required
def volunteer_update(request, hashid):
    objects = get_object_or_404(Volunteer, hashed=hashid)
    if request.method == 'POST':
        form = VolunteerForm(request.POST, request.FILES, instance=objects)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, f'Successfully Update Volunteer')
            return redirect('admin-volunteer-list')
    else:
        form = VolunteerForm(instance=objects)
    context = {
        'title': 'Altera Internship','subtitle': 'Internship', 'form': form
    }
    return render(request, 'volunteer/form.html', context)

@login_required
def volunteer_detail(request, hashid):
    objects = get_object_or_404(Volunteer, hashed=hashid)
    context = {
        'title': 'Detail Volunteer', 'subtitle': 'Volunteer', 'objects': objects
    }
    return render(request, 'volunteer/detail.html', context)

@login_required
def volunteer_activate(request, hashid):
    objects = get_object_or_404(Volunteer, hashed=hashid)
    objects.is_active = True
    objects.save()
    messages.success(request, 'Successfully Activate Internship')
    return redirect('admin-volunteer-list')

@login_required
def volunteer_deactivate(request, hashid):
    objects = get_object_or_404(Volunteer, hashed=hashid)
    objects.is_active = False
    objects.save()
    messages.success(request, 'Successfully Deactivate Internship')
    return redirect('admin-volunteer-list')