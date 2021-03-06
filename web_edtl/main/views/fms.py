import email
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth import authenticate
from main.forms import FMSLoginForm, BillForm
from django.contrib.auth import authenticate, login
from custom.decorators import allowed_users
from django.contrib.auth.decorators import login_required
from finance.models import Client, Bill
from main.utils import getnewid, title_seo
from django.contrib import messages
from datetime import datetime
from custom.forms import UserUpdateForm
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
from django.urls import reverse_lazy
from main.models import User
import re
from news.tasks import finance_incomming


def fms_login(request):
    form = FMSLoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_client:
                login(request,user)
                return redirect('client-home')
            else:
                msg = 'Invalid Credential'
        else:
            msg = 'Eror Validation'
    context = {
        'form': form, 'msg':msg
    }
    return render(request, 'fms/login.html', context)
    
@login_required
@allowed_users(allowed_roles=['client'])
def client_home(request):
    title = 'Client Dashboard'
    context = {
        'title': title
    }
    return render(request, 'fms/dashboard.html', context)
    
@login_required
@allowed_users(allowed_roles=['client'])
def client_bill_list(request):
    client = get_object_or_404(Client, user=request.user)
    bills = Bill.objects.filter(is_done=False,client=client).order_by('-upload_date')
    bills_dones = Bill.objects.filter(is_done=True,client=client).order_by('-upload_date')
    context = {
        'title': 'Bill Lists','bills': bills, 'bills_dones':bills_dones
    }
    return render(request, 'fms/list.html', context)


@login_required
@allowed_users(allowed_roles=['client'])
def client_bill_add(request):
    group = request.user.groups.all()[0].name
    client = get_object_or_404(Client, user=request.user)
    if request.method == 'POST':
        newid, new_hashed = getnewid(Bill)
        form = BillForm(request.POST, request.FILES)
        fullname = client.name
        finance = User.objects.filter(groups__name='finance', is_active=True)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id = newid
            instance.client = client
            instance.hashed = new_hashed
            instance.upload_date = datetime.now()
            instance.save()
            for email_to in finance:
                set_name = email_to.email
                print(set_name)
                set_name2 = re.split(r'[@.]', set_name)
                finance_incomming.delay(email_to.email,set_name2[0],fullname)
            messages.success(request, f'Successfully Add Bill')
            return redirect('bill-list')
    else:
        form = BillForm()
    context = {
        'title': 'Add Bill','subtitle': 'Bill', 'form': form,
        'group': group
    }
    return render(request, 'fms/form.html', context)

@login_required
@allowed_users(allowed_roles=['client'])
def client_bill_update(request,hashid):
    group = request.user.groups.all()[0].name
    objects = get_object_or_404(Bill, hashed=hashid)
    if request.method == 'POST':
        form = BillForm(request.POST, request.FILES, instance=objects)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully Update Bill')
            return redirect('bill-list')
    else:
        form = BillForm(instance=objects)
    context = {
        'title': 'Update Bill','subtitle': 'Bill', 'form': form,
        'group': group
    }
    return render(request, 'fms/form.html', context)

@login_required
@allowed_users(allowed_roles=['client'])
def client_bill_delete(request,hashid):
    objects = get_object_or_404(Bill,hashed=hashid)
    objects.delete()
    messages.success(request, f'Successfully Delete Image')
    return redirect('bill-list')

@login_required
@allowed_users(allowed_roles=['client'])
def client_bill_detail(request, hashid):
    group = request.user.groups.all()[0].name
    objects = get_object_or_404(Bill, hashed=hashid)
    context = {
        'title': 'Detail Bill', 'subtitle': 'Bill', 'objects': objects,
        'group': group,
    }
    return render(request, 'fms/detail.html', context)


@login_required
@allowed_users(allowed_roles=['client'])
def AccountUpdate(request):
	group = request.user.groups.all()[0].name
	objects = User.objects.get(pk=request.user.pk)
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		if u_form.is_valid():
			u_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('user-account')
	else:
		u_form = UserUpdateForm(instance=request.user)

	context = {
		'u_form': u_form,
		'title': 'ACCOUNT INFO',
		'legend': 'ACCOUNT INFO',
		'title_page': 'Account Info',
		'group': group
	}
	return render(request, 'fms/account.html', context)

class UserPasswordChangeView(PasswordChangeView):
	template_name = 'fms/change_password.html'
	success_url = reverse_lazy('user-change-password-done')

class UserPasswordChangeDoneView(PasswordResetDoneView):
	template_name = 'fms/change_password_done.html'