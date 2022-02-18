from django.shortcuts import render, redirect, get_object_or_404
from report.models import Report
from report.forms import ReportForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.utils import getnewid
from django.contrib import messages
from custom.decorators import allowed_users


@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def report_list(request):
    group = request.user.groups.all()[0].name
    objects = Report.objects.all().order_by('-datetime')
    context = {
        'objects': objects,'group': group, 'title': 'Lista Relatorio',
    }
    return render(request, 'report/list.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def report_add(request):
    group = request.user.groups.all()[0].name
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
        'title': 'Aumenta Relatorio','group': group,'subtitle': 'Relatorio', 'form': form
    }
    return render(request, 'report/form.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def report_update(request, hashid):
    group = request.user.groups.all()[0].name
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
        'title': 'Altera Relatorio','group': group,'subtitle': 'Relatorio', 'form': form
    }
    return render(request, 'report/form.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media','coordinator'])
def report_detail(request, hashid):
    group = request.user.groups.all()[0].name
    objects = get_object_or_404(Report, hashed=hashid)
    context = {
        'title': 'Detail Report','group': group, 'subtitle': 'Report', 'objects': objects
    }
    return render(request, 'report/detail.html', context)

@login_required
@allowed_users(allowed_roles=['admin','media'])
def report_activate(request, hashid):
    objects = get_object_or_404(Report, hashed=hashid)
    objects.is_active = True
    objects.save()
    messages.success(request, 'Successfully Activate Report')
    return redirect('admin-report-list')

@login_required
@allowed_users(allowed_roles=['admin','media'])
def report_deactivate(request, hashid):
    objects = get_object_or_404(Report, hashed=hashid)
    objects.is_active = False
    objects.save()
    messages.success(request, 'Successfully Deactivate Report')
    return redirect('admin-report-list')