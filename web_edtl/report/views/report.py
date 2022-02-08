from django.shortcuts import render, redirect, get_object_or_404
from report.models import Report
from report.forms import ReportForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from django.conf import settings
from main.utils import getnewid
from django.contrib import messages
from datetime import date

@login_required
def report_list(request):
    objects = Report.objects.all().order_by('-datetime')
    context = {
        'objects': objects, 'title': 'Lista Relatorio',
    }
    return render(request, 'report/list.html', context)

@login_required
def report_add(request):
    if request.method == 'POST':
        newid, new_hashed = getnewid(Report)
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id = newid
            instance.author = request.user
            instance.hashed = new_hashed
            instance.save()
            messages.success(request, f'Successfully Add Report')
            return redirect('admin-report-list')
    else:
        form = ReportForm()
    context = {
        'title': 'Aumenta Relatorio','subtitle': 'Relatorio', 'form': form
    }
    return render(request, 'report/form.html', context)

@login_required
def report_update(request, hashid):
    objects = get_object_or_404(Report, hashed=hashid)
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES, instance=objects)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, f'Successfully Update Report')
            return redirect('admin-report-list')
    else:
        form = ReportForm(instance=objects)
    context = {
        'title': 'Altera Relatorio','subtitle': 'Relatorio', 'form': form
    }
    return render(request, 'report/form.html', context)

@login_required
def report_detail(request, hashid):
    objects = get_object_or_404(Report, hashed=hashid)
    context = {
        'title': 'Detail Report', 'subtitle': 'Report', 'objects': objects
    }
    return render(request, 'report/detail.html', context)

@login_required
def report_activate(request, hashid):
    objects = get_object_or_404(Report, hashed=hashid)
    objects.is_active = True
    objects.save()
    messages.success(request, 'Successfully Activate Report')
    return redirect('admin-report-list')

@login_required
def report_deactivate(request, hashid):
    objects = get_object_or_404(Report, hashed=hashid)
    objects.is_active = False
    objects.save()
    messages.success(request, 'Successfully Deactivate Report')
    return redirect('admin-report-list')