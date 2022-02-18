from django.shortcuts import render, redirect, get_object_or_404
from faq.models import Faq
from faq.forms import FaqForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.utils import getnewid
from django.contrib import messages
from custom.decorators import allowed_users

@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def faq_list(request):
    group = request.user.groups.all()[0].name
    objects = Faq.objects.all()
    context = {
        'objects': objects, 'title': 'Lista FAQ', 'group': group, 
    }
    return render(request, 'faq/list.html',context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def faq_add(request):
    group = request.user.groups.all()[0].name
    if request.method == 'POST':
        newid, new_hashed = getnewid(Faq)
        form = FaqForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id = newid
            instance.author = request.user
            instance.hashed = new_hashed
            instance.save()
            messages.success(request, f'Successfully Add Faq')
            return redirect('admin-faq-list')
    else:
        form = FaqForm()
    context = {
        'title': 'Aumenta Faq','subtitle': 'Faq', 'form': form, 'group': group, 
    }
    return render(request, 'faq/form.html', context)


@login_required
@allowed_users(allowed_roles=['admin','media'])
def faq_update(request, hashid):
    group = request.user.groups.all()[0].name
    objects = get_object_or_404(Faq, hashed=hashid)
    if request.method == 'POST':
        form = FaqForm(request.POST, request.FILES, instance=objects)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, f'Successfully Update Faq')
            return redirect('admin-faq-list')
    else:
        form = FaqForm(instance=objects)
    context = {
        'title': 'Altera Faqo','subtitle': 'Faqo', 'form': form, 'group': group, 
    }
    return render(request, 'faq/form.html', context)


@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def faq_detail(request, hashid):
    group = request.user.groups.all()[0].name
    objects = get_object_or_404(Faq, hashed=hashid)
    context = {
        'title': 'Detail Faq', 'subtitle': 'Faq', 'objects': objects, 'group': group, 
    }
    return render(request, 'faq/detail.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def faq_activate(request, hashid):
    objects = get_object_or_404(Faq, hashed=hashid)
    objects.is_active = True
    objects.save()
    messages.success(request, 'Successfully Activate Faq')
    return redirect('admin-faq-list')

@login_required
@allowed_users(allowed_roles=['admin','media'])
def faq_deactivate(request, hashid):
    objects = get_object_or_404(Faq, hashed=hashid)
    objects.is_active = False
    objects.save()
    messages.success(request, 'Successfully Deactivate Faq')
    return redirect('admin-faq-list')

@login_required
@allowed_users(allowed_roles=['admin','media'])
def faq_set_homepage(request, hashid):
    objects = get_object_or_404(Faq, hashed=hashid)
    objects.is_homepage = True
    objects.save()
    messages.success(request, 'Successfully Set Faq to Homepage')
    return redirect('admin-faq-list')

@login_required
@allowed_users(allowed_roles=['admin','media'])
def faq_remove_homepage(request, hashid):
    objects = get_object_or_404(Faq, hashed=hashid)
    objects.is_homepage = False
    objects.save()
    messages.success(request, 'Successfully Remove Faq from Homepage')
    return redirect('admin-faq-list')