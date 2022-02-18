from django.shortcuts import render, redirect, get_object_or_404
from recruitment.models import Volunteer
from recruitment.forms import VolunteerForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.utils import getnewid
from django.contrib import messages
from custom.decorators import allowed_users

@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def volunteer_list(request):
    group = request.user.groups.all()[0].name
    objects = Volunteer.objects.all().order_by('-datetime')
    context = {
        'objects': objects,'group': group, 'title': 'Lista Vaga',
    }
    return render(request, 'volunteer/list.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def volunteer_add(request):
    group = request.user.groups.all()[0].name
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
        'title': 'Aumenta Internship','group': group,'subtitle': 'Internship', 'form': form
    }
    return render(request, 'volunteer/form.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def volunteer_update(request, hashid):
    group = request.user.groups.all()[0].name
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
        'title': 'Altera Internship','group': group,'subtitle': 'Internship', 'form': form
    }
    return render(request, 'volunteer/form.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def volunteer_detail(request, hashid):
    group = request.user.groups.all()[0].name
    objects = get_object_or_404(Volunteer, hashed=hashid)
    context = {
        'title': 'Detail Volunteer','group': group, 'subtitle': 'Volunteer', 'objects': objects
    }
    return render(request, 'volunteer/detail.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def volunteer_activate(request, hashid):
    objects = get_object_or_404(Volunteer, hashed=hashid)
    objects.is_active = True
    objects.save()
    messages.success(request, 'Successfully Activate Internship')
    return redirect('admin-volunteer-list')

@login_required
@allowed_users(allowed_roles=['admin','media'])
def volunteer_deactivate(request, hashid):
    objects = get_object_or_404(Volunteer, hashed=hashid)
    objects.is_active = False
    objects.save()
    messages.success(request, 'Successfully Deactivate Internship')
    return redirect('admin-volunteer-list')