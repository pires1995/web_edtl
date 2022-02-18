from django.shortcuts import render, redirect, get_object_or_404
from recruitment.models import Internships
from recruitment.forms import InternshipsForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.utils import getnewid
from django.contrib import messages
from custom.decorators import allowed_users

@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def internships_list(request):
    group = request.user.groups.all()[0].name
    objects = Internships.objects.all().order_by('-datetime')
    context = {
        'objects': objects,'group': group, 'title': 'Lista Vaga',
    }
    return render(request, 'internships/list.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def internships_add(request):
    if request.method == 'POST':
        group = request.user.groups.all()[0].name
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
        'title': 'Aumenta Internship','group': group,'subtitle': 'Internship', 'form': form
    }
    return render(request, 'internships/form.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def internships_update(request, hashid):
    group = request.user.groups.all()[0].name
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
        'title': 'Altera Internship','group': group,'subtitle': 'Internship', 'form': form
    }
    return render(request, 'internships/form.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def internships_detail(request, hashid):
    group = request.user.groups.all()[0].name
    objects = get_object_or_404(Internships, hashed=hashid)
    context = {
        'title': 'Detail Internships','group': group, 'subtitle': 'Internships', 'objects': objects
    }
    return render(request, 'internships/detail.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def internships_activate(request, hashid):
    objects = get_object_or_404(Internships, hashed=hashid)
    objects.is_active = True
    objects.save()
    messages.success(request, 'Successfully Activate Internship')
    return redirect('admin-internships-list')

@login_required
@allowed_users(allowed_roles=['admin','media'])
def internships_deactivate(request, hashid):
    objects = get_object_or_404(Internships, hashed=hashid)
    objects.is_active = False
    objects.save()
    messages.success(request, 'Successfully Deactivate Internship')
    return redirect('admin-internships-list')