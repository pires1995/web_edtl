from django.shortcuts import render, redirect, get_object_or_404
from finance.models import Client
from finance.forms import ClientForm
from finance.utils import getid
from django.contrib.auth.models import Group
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.utils import getnewid
import re
from main.models import User
from custom.decorators import allowed_users

@login_required
@allowed_users(allowed_roles=['finance'])
def client_list(request):
    group = request.user.groups.all()[0].name
    users = Client.objects.all()
    # usergroup = request.user.groups.all()[0].name
    context = {
        'users': users, 'title': 'Client List','group': group, 
    }
    return render(request, 'client/list.html', context)

@login_required
@allowed_users(allowed_roles=['finance'])
def client_add(request):
    group = request.user.groups.all()[0].name
    if request.method == 'POST':
        newid, new_hashed = getnewid(Client)
        userid = getid(User)
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id = newid
            instance.hashed = new_hashed
            pass_set = form.cleaned_data['email']
            pass_set2 = re.split(r'[@.]',pass_set)
            passnew = pass_set2[0] + str(userid)
            password = make_password(passnew)
            instance.temp_password = passnew
            objuser = User(id=userid, email=instance.email, password=password, is_client=True, is_staff=False)
            objuser.save()
            instance.user = User.objects.get(pk=userid)
            instance.save()
            usergroup = Group.objects.get(name='client')
            user = User.objects.get(pk=userid)
            user.groups.add(usergroup)
            # instance.save()
            messages.success(request, f'Successfully Add Client')
            return redirect('admin-client-list')
    else:
        form = ClientForm()
    context = {
        'title': 'Aumenta Cliente','subtitle': 'Client', 'form': form,'group': group, 
    }
    return render(request, 'client/form.html', context)

@login_required
@allowed_users(allowed_roles=['finance'])
def client_detail(request, hashid):
    group = request.user.groups.all()[0].name
    objects = get_object_or_404(Client, hashed=hashid)
    context = {
        'title': 'Detail Client', 'subtitle': 'Client', 'objects': objects,'group': group, 
    }
    return render(request, 'client/detail.html', context)