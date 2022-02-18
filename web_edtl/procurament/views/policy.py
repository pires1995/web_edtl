from django.shortcuts import render, redirect, get_object_or_404
from procurament.models import Policy
from procurament.forms import PolicyForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from django.conf import settings
from main.utils import getnewid
from django.contrib import messages
from custom.decorators import allowed_users


@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def policy_list(request):
    group = request.user.groups.all()[0].name
    objects = Policy.objects.all().order_by('-datetime')
    context = {
        'objects': objects, 'title': 'Lista Policy', 'group':group
    }
    return render(request, 'policy/list.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def policy_add(request):
    group = request.user.groups.all()[0].name
    if request.method == 'POST':
        newid, new_hashed = getnewid(Policy)
        form = PolicyForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id = newid
            instance.author = request.user
            instance.hashed = new_hashed
            instance.save()
            messages.success(request, f'Successfully Add Policy')
            return redirect('admin-policy-list')
    else:
        form = PolicyForm()
    context = {
        'title': 'Aumenta Policy', 'group':group, 'subtitle': 'Policy', 'form': form
    }
    return render(request, 'policy/form.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def policy_update(request, hashid):
    group = request.user.groups.all()[0].name
    objects = get_object_or_404(Policy, hashed=hashid)
    if request.method == 'POST':
        form = PolicyForm(request.POST, request.FILES, instance=objects)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, f'Successfully Update Policy')
            return redirect('admin-policy-list')
    else:
        form = PolicyForm(instance=objects)
    context = {
        'title': 'Altera Policy', 'group':group, 'subtitle': 'Policy', 'form': form
    }
    return render(request, 'policy/form.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def policy_detail(request, hashid):
    group = request.user.groups.all()[0].name
    objects = get_object_or_404(Policy, hashed=hashid)
    context = {
        'title': 'Detail Policy', 'group':group, 'subtitle': 'Policy', 'objects': objects
    }
    return render(request, 'policy/detail.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def policy_activate(request, hashid):
    objects = get_object_or_404(Policy, hashed=hashid)
    objects.is_active = True
    objects.save()
    messages.success(request, 'Successfully Activate Policy')
    return redirect('admin-policy-list')

@login_required
@allowed_users(allowed_roles=['admin','media'])
def policy_deactivate(request, hashid):
    objects = get_object_or_404(Policy, hashed=hashid)
    objects.is_active = False
    objects.save()
    messages.success(request, 'Successfully Deactivate Policy')
    return redirect('admin-policy-list')