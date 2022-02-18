import email
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth import authenticate
from main.forms import FMSLoginForm, BillForm, USMForm
from django.contrib.auth import authenticate, login
from custom.decorators import allowed_users
from django.contrib.auth.decorators import login_required
from news.models import SubscribeChoice, NewsUser
from main.utils import getnewid, title_seo
from django.contrib import messages
from datetime import datetime
from main.utils_lang import lang_master
from departments.models import Department
from product.models import Product

def usm_login(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    form = USMForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data.get('email')
            try:

                usersubscribe = NewsUser.objects.get(email=email)
                print(usersubscribe)
                if usersubscribe:
                    context = {
                        'usersubscribe':usersubscribe,'lang':lang, 'l1': 'tt', 'l2': 'pt', 'l3': 'en'
                    }
                    return render(request, 'usm/dashboard.html', context)
                else:
                    messages.error(request, f'Sorry, we cannot find your Email!')
                    return redirect('usm-login', lang)
            except:
                    messages.error(request, f'Sorry, we cannot find your Email!')
                    return redirect('usm-login', lang)
                

        else:
            messages.error(request, f'Upps, Something Wrong')
            return redirect('usm-login', lang)
    context = {
        'form': form,'departments':departments,'products': products, 'lang_data': lang_data, \
            'lang':lang, 'l1': 'tt', 'l2': 'pt', 'l3': 'en'
    }
    return render(request, 'usm/login.html', context)
@login_required
@allowed_users(allowed_roles=['client'])
def client_home(request):
    title = 'Client Dashboard'
    context = {
        'title': title
    }
    return render(request, 'usm/dashboard.html', context)
    
@login_required
@allowed_users(allowed_roles=['client'])
def client_bill_list(request):
    client = get_object_or_404(Client, user=request.user)
    bills = Bill.objects.filter(is_done=False,client=client).order_by('-upload_date')
    bills_dones = Bill.objects.filter(is_done=True,client=client).order_by('-upload_date')
    context = {
        'title': 'Bill Lists','bills': bills, 'bills_dones':bills_dones
    }
    return render(request, 'usm/list.html', context)


@login_required
@allowed_users(allowed_roles=['client'])
def client_bill_add(request):
    group = request.user.groups.all()[0].name
    client = get_object_or_404(Client, user=request.user)
    if request.method == 'POST':
        newid, new_hashed = getnewid(Bill)
        form = BillForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id = newid
            instance.client = client
            instance.hashed = new_hashed
            instance.upload_date = datetime.now()
            instance.save()
            messages.success(request, f'Successfully Add Bill')
            return redirect('bill-list')
    else:
        form = BillForm()
    context = {
        'title': 'Add Bill','subtitle': 'Bill', 'form': form,
        'group': group
    }
    return render(request, 'usm/form.html', context)

@login_required
@allowed_users(allowed_roles=['client'])
def client_bill_detail(request, hashid):
    group = request.user.groups.all()[0].name
    objects = get_object_or_404(Bill, hashed=hashid)
    context = {
        'title': 'Detail Bill', 'subtitle': 'Bill', 'objects': objects,
        'group': group,
    }
    return render(request, 'usm/detail.html', context)
