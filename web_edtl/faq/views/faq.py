from django.shortcuts import render, redirect, get_object_or_404
from faq.models import Faq
from faq.forms import FaqForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from django.conf import settings
from main.utils import getnewid
from django.contrib import messages


@login_required
def faq_list(request):
    objects = Faq.objects.all()
    context = {
        'objects': objects, 'title': 'Lista FAQ'
    }
    return render(request, 'faq/list.html',context)

def faq_add(request):
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
        'title': 'Aumenta Faq','subtitle': 'Faq', 'form': form
    }
    return render(request, 'faq/form.html', context)


@login_required
def faq_update(request, hashid):
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
        'title': 'Altera Faqo','subtitle': 'Faqo', 'form': form
    }
    return render(request, 'faq/form.html', context)


@login_required
def faq_detail(request, hashid):
    objects = get_object_or_404(Faq, hashed=hashid)
    context = {
        'title': 'Detail Faq', 'subtitle': 'Faq', 'objects': objects
    }
    return render(request, 'faq/detail.html', context)