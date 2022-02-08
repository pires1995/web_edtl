from django.shortcuts import render, redirect, get_object_or_404
from project.models import Project, ProjectBudget, ProjectLocation
from project.forms import NewProjectForm, ProjectBudgetForm, ProjectLocationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from django.conf import settings
from main.utils import getnewid
from django.contrib import messages


@login_required
def new_project_list(request):
    objects = Project.objects.filter(project_status = 1).order_by('-datetime')
    context = {
        'objects': objects, 'title': 'Lista Projetu Foun',
    }
    return render(request, 'new/list.html', context)

@login_required
def new_project_add(request):
    if request.method == 'POST':
        newid, new_hashed = getnewid(Project)
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id = newid
            instance.author = request.user
            instance.hashed = new_hashed
            instance.save()
            messages.success(request, f'Successfully Add Project')
            return redirect('admin-new-project-list')
    else:
        form = NewProjectForm()
    context = {
        'title': 'Aumenta Projetu','subtitle': 'Projetu', 'form': form
    }
    return render(request, 'new/form.html', context)

@login_required
def new_project_update(request, hashid):
    objects = get_object_or_404(Project, hashed=hashid)
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES, instance=objects)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, f'Successfully Update Project')
            return redirect('admin-new-project-list')
    else:
        form = NewProjectForm(instance=objects)
    context = {
        'title': 'Altera Porjetu','subtitle': 'Projetu', 'form': form
    }
    return render(request, 'new/form.html', context)

@login_required
def new_project_detail(request, hashid):
    location = None
    budget = None
    try:
        objects = get_object_or_404(Project, hashed=hashid)
        budget = get_object_or_404(ProjectBudget, project=objects)
        location = get_object_or_404(ProjectLocation, project=objects)
    except:
        objects = get_object_or_404(Project, hashed=hashid)
    context = {
        'title': 'Detail Project', 'subtitle': 'Project', \
            'objects': objects, 'location': location, 'budget': budget
    }
    return render(request, 'new/detail.html', context)

@login_required
def new_project_add_budget(request, hashid):
    objects = get_object_or_404(Project, hashed=hashid)
    if request.method == 'POST':
        newid, new_hashed = getnewid(ProjectBudget)
        form = ProjectBudgetForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.project = objects
            instance.id = newid
            instance.author = request.user
            instance.hashed = new_hashed
            instance.save()
            messages.success(request, f'Successfully Add Project Budget')
            return redirect('admin-new-project-detail', hashid=hashid )
        else:
            form = ProjectBudgetForm()
    context = {
        'title': 'Aumenta Project Budget','subtitle': 'Budget Projetu', 'form': form
    }
    return render(request, 'budget/form.html', context)

@login_required
def new_project_add_location(request, hashid):
    objects = get_object_or_404(Project, hashed=hashid)
    if request.method == 'POST':
        newid, new_hashed = getnewid(ProjectLocation)
        form = ProjectLocationForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.project = objects
            instance.id = newid
            instance.author = request.user
            instance.hashed = new_hashed
            instance.save()
            messages.success(request, f'Successfully Add Project Location')
            return redirect('admin-new-project-detail', hashid=hashid)
    else:
        form = ProjectLocationForm()
    context = {
        'title': 'Aumenta Project Location','subtitle': 'Project Location', 'form': form
    }
    return render(request, 'location/form.html', context)

@login_required
def new_project_update_location(request, hashid, hashid2):
    objects = get_object_or_404(Project, hashed=hashid)
    objectloc = get_object_or_404(ProjectLocation, hashed=hashid2)
    if request.method == 'POST':
        form = ProjectLocationForm(request.POST, request.FILES, instance=objectloc)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.project = objects
            instance.author = request.user
            instance.save()
            messages.success(request, f'Successfully Update Project Location')
            return redirect('admin-new-project-detail', hashid=hashid)
    else:
        form = ProjectLocationForm(instance=objectloc)
    context = {
        'title': 'Altera Project Location','subtitle': 'Project Location', 'form': form
    }
    return render(request, 'location/form.html', context)

@login_required
def new_project_update_budget(request, hashid, hashid2):
    objects = get_object_or_404(Project, hashed=hashid)
    objectloc = get_object_or_404(ProjectBudget, hashed=hashid2)
    if request.method == 'POST':
        form = ProjectBudgetForm(request.POST, request.FILES, instance=objectloc)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.project = objects
            instance.author = request.user
            instance.save()
            messages.success(request, f'Successfully Update Project Budget')
            return redirect('admin-new-project-detail', hashid=hashid)
    else:
        form = ProjectBudgetForm(instance=objectloc)
    context = {
        'title': 'Altera Project Budget','subtitle': 'Project Budget', 'form': form
    }
    return render(request, 'budget/form.html', context)

@login_required
def new_project_activate(request, hashid):
    objects = get_object_or_404(Project, hashed=hashid)
    objects.is_active = True
    objects.save()
    messages.success(request, 'Successfully Activate Project')
    return redirect('admin-new-project-list')

@login_required
def new_project_deactivate(request, hashid):
    objects = get_object_or_404(Project, hashed=hashid)
    objects.is_active = False
    objects.save()
    messages.success(request, 'Successfully Deactivate Project')
    return redirect('admin-new-project-list')