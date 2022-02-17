from __future__ import division
from cmath import log
from django.shortcuts import render, redirect, get_object_or_404
from profiles.models import About, Division, Employee, Position
from profiles.forms import EmployeeForm, DivisionProfileForm, PositionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from django.conf import settings
from main.utils import getnewid


def add_employee(request):
    if request.method == 'POST':
        newid, new_hashed = getnewid(Employee)
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id = newid
            instance.hashed = new_hashed
            instance.save()
            messages.success(request, f'Successfully Create Employee')
            return redirect('admin-team-list')
    else:   
        form = EmployeeForm()
    context = {
        'form': form, 'title': 'Aumenta Informasaun Empregu', 'subtitle': 'Empregu'
    }
    return render(request, 'team/form.html', context)

def update_employee(request, hashid):
  objects = get_object_or_404(Employee, hashed=hashid)
  if request.method == 'POST':
      form = EmployeeForm(request.POST, request.FILES, instance=objects)
      if form.is_valid():
          form.save()
          messages.success(request, f'Successfully Update Employee')
          return redirect('admin-team-list')
  else:   
      form = EmployeeForm(instance=objects)
  context = {
      'form': form, 'title': 'Altera Informasaun Empregu', 'subtitle': 'Empregu'
  }
  return render(request, 'team/form.html', context)

@login_required
def list_team(request):
    group = request.user.groups.all()[0].name
    organograma = Position.objects.all()
    employees = Employee.objects.all()
    divisions = Division.objects.all()
    boardmembers = Position.objects.filter(group='Board Member')
    departments = Position.objects.filter(group='Department')
    divisions_board = Position.objects.filter(group='Division')
    context = {
        'title': 'Lista Organograma', 'group': group, 'boardmembers': boardmembers, 'departments':departments,
        'employees': employees, 'divisions': divisions, 'divisions_board':divisions_board
    }
    return render(request, 'team/team_list.html', context)

@login_required
def add_team(request):
    if request.method == 'POST':
        newid, new_hashed = getnewid(Position)
        form = PositionForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id = newid
            instance.hashed = new_hashed
            instance.save()
            messages.success(request, f'Successfully Create Position')
            return redirect('admin-team-list')
    else:   
        form = PositionForm()
    context = {
        'form': form, 'title': 'Aumenta Informasaun Pozisaun', 'subtitle': 'Pozisaun'
    }
    return render(request, 'team/form.html', context)

@login_required
def update_team(request, hashid):
  objects = get_object_or_404(Position, hashed=hashid)
  if request.method == 'POST':
      form = PositionForm(request.POST, request.FILES, instance=objects)
      if form.is_valid():
          form.save()
          messages.success(request, f'Successfully Update Position')
          return redirect('admin-team-list')
  else:   
      form = PositionForm(instance=objects)
  context = {
      'form': form, 'title': 'Altera Informasaun Pozisaun', 'subtitle': 'Pozisaun'
  }
  return render(request, 'team/form.html', context)


@login_required
def add_division_profile(request):
    if request.method == 'POST':
        newid, new_hashed = getnewid(Division)
        form = DivisionProfileForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id = newid
            instance.hashed = new_hashed
            instance.save()
            messages.success(request, f'Successfully Create Division')
            return redirect('admin-team-list')
    else:   
        form = DivisionProfileForm()
    context = {
        'form': form, 'title': 'Aumenta Informasaun Divisaun', 'subtitle': 'Divisaun'
    }
    return render(request, 'team/form.html', context)

@login_required
def update_division_profile(request, hashid):
  objects = get_object_or_404(Division, hashed=hashid)
  if request.method == 'POST':
      form = DivisionProfileForm(request.POST,instance=objects)
      if form.is_valid():
          form.save()
          messages.success(request, f'Successfully Update Division')
          return redirect('admin-team-list')
  else:   
      form = DivisionProfileForm(instance=objects)
  context = {
      'form': form, 'title': 'Altera Informasaun Divisaun', 'subtitle': 'Divisaun'
  }
  return render(request, 'team/form.html', context)

