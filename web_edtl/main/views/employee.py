from django.shortcuts import render, redirect, get_object_or_404
from main.models import User
from main.forms import CustomUserForm
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def user_lists(request):
    group = request.user.groups.all()[0].name
    users = User.objects.all().exclude(groups__name='client')
    # usergroup = request.user.groups.all()[0].name
    context = {
        'users': users,'group': group, 'title': 'Users List',
    }
    return render(request, 'employee/users_list.html', context)


@login_required
def user_add(request):
    group = request.user.groups.all()[0].name
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            gp = request.POST.get('groups')
            group = Group.objects.get(id=gp)
            instance.set_password('edtl#2022')
            instance.save()
            instance.groups.add(group)
            messages.success(
                request, f'User {instance.email} Successfully Created')
            return redirect('admin-user-lists')
    context = {
        'form': form,'group': group, 'title': 'Add User',
    }
    return render(request, 'employee/add.html', context)


@login_required
def user_update(request, hashid):
    group = request.user.groups.all()[0].name
    object = get_object_or_404(User, hashed=hashid)
    if request.method == 'POST':
        form = CustomUserForm(request.POST, instance=object)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.groups.clear()
            gp = request.POST.get('groups')
            group = Group.objects.get(id=gp)
            instance.groups.add(group)
            instance.save()
            messages.success(
                request, f'User {instance.email} Successfully Update')
            return redirect('admin-user-lists')
    else:
        form = CustomUserForm(instance=object)
    context = {
        'form': form,'group': group, 'title': 'Update User',
    }
    return render(request, 'employee/add.html', context)


@login_required
def user_activate(request, hashid):
    object = get_object_or_404(User, hashed=hashid)
    object.is_active = True
    object.save()
    messages.success(request, f'User {object.email} Successfully Activate')
    return redirect('admin-user-lists')


@login_required
def user_deactivate(request, hashid):
    object = get_object_or_404(User, hashed=hashid)
    object.is_active = False
    object.save()
    messages.warning(request, f'User {object.email} Successfully Deactivate')
    context = {}
    return redirect('admin-user-lists')
