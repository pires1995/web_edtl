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
    group = request.user.groups.all()[0].name
    departments = Department.objects.all()
    subscribechoices = SubscribeChoice.objects.all()
    products = Product.objects.filter(is_active=True)
    form = USMForm(request.POST or None)
    if 'usm_form' in request.POST:
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                objects = get_object_or_404(NewsUser, email=email)
                return render(request, 'usm/dashboard.html',{'lang': lang,\
                    'l1': 'tt', 'l2': 'pt', 'l3': 'en', 'products':products,\
                    'departments':departments, 'lang_data':lang_data, 'usersubscribe': objects,\
                         'subscribechoices':subscribechoices})
            except:
                messages.error(request, f'Sorry, we cannot find your Email!')
                return redirect('usm-login', lang)
    elif 'usm_subscribe' in request.POST:
        email2 = request.POST.get('email')
        choice = request.POST.getlist('choices')
        all_choice = SubscribeChoice.objects.all()

        objects = get_object_or_404(NewsUser, email=email2)
        objects.choices.clear()
        for i in choice:
            objects.choices.add(i)
            objects.save()
            

        return render(request, 'usm/dashboard.html',{'lang': lang,\
            'l1': 'tt', 'l2': 'pt', 'l3': 'en', 'products':products,\
            'departments':departments, 'lang_data':lang_data, 'usersubscribe': objects,\
                    'subscribechoices':subscribechoices})

    context = {
        'form': form,'departments':departments,'products': products, 'lang_data': lang_data, \
            'lang':lang, 'l1': 'tt', 'l2': 'pt', 'l3': 'en'
    }
    return render(request, 'usm/login.html', context)

@login_required
@allowed_users(allowed_roles=['client'])
def usm_home(request, lang, hashid):
    print(hashid)
    title = 'Client Dashboard'
    lang_data = lang_master(lang)
    context = {
        'title': title, 'lang':lang, 'l1': 'tt', 'l2': 'pt', 'l3': 'en', 'lang_data':lang_data
    }
    return render(request, 'usm/dashboard.html', context)

@login_required
def usm_choices(request, lang, hashid):
    title = 'Client Dashboard'
    if request.method == 'POST':
        form = request.POST.getlist('choices')
        print(form)
    objects = get_object_or_404(NewsUser, hashed=hashid)
    subscribechoices = SubscribeChoice.objects.all()
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    lang_data = lang_master(lang)
    return render(request, 'usm/dashboard.html',{'lang': lang,\
                'l1': 'tt', 'l2': 'pt', 'l3': 'en', 'products':products,\
                 'departments':departments, 'lang_data':lang_data, 'usersubscribe': objects, 'subscribechoices':subscribechoices})
    
@login_required
def usm_unsubscribe(request, lang,year,day,hour,minute, hashid):
    lang_data = lang_master(lang)
    subscribechoices = SubscribeChoice.objects.all()
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    objects = NewsUser.objects.get(hashed=hashid)
    objects.delete()
    messages.success(request, 'Successfully Unsubscribe')
    return redirect('redirect-home')

def usm_login2(request,lang):
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
                context = {
                    'usersubscribe':usersubscribe,'lang':lang, 'l1': 'tt', 'l2': 'pt', 'l3': 'en'
                }
                return render(request, 'usm/dashboard.html', context)
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
