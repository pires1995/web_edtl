from django.shortcuts import render, redirect, get_object_or_404
from main.utils_lang import lang_master
from departments.models import Department, Division
from product.models import Product
from procurament.models import Tender, Guidelines, Policy
from datetime import datetime
from django.core.paginator import Paginator
from django.http import FileResponse
from django.conf import settings
from pagemanegament.models import PageManegament
from custom.models import IpModel
from main.utils import get_client_ip
from datetime import datetime

def tender_list(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    today = datetime.now()
    objects = Tender.objects.filter(is_active=True).order_by('-datetime')
    lang_data = lang_master(lang)
    paginator = Paginator(objects, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    today = datetime.now().date()
    ip = get_client_ip(request)
    if IpModel.objects.filter(ip=ip).exists():
        if IpModel.objects.filter(ip=ip, datetime__date=today):
            pass
        else:
            IpModel.objects.create(ip=ip)
    else:
        IpModel.objects.create(ip=ip)
    if lang == 'tt':
        titlepage='EDTL.EP - Lista Tender'
    elif lang == 'pt':
        titlepage='EDTL.EP - Lista Tender'
    else:
        titlepage='EDTL.EP - Tender List'
    try:
        page_description = get_object_or_404(PageManegament, name='tender',is_active = True)
    except:
        page_description = ''
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,\
                 'page_obj':page_obj, 'titlepage':titlepage, 'today': today, 'page_description': page_description
    }
    template = 'inner_page/procurament/tender.html'
    return render(request, template, context)

def tender_download(request, hashid):
	obj = get_object_or_404(Tender, hashed=hashid)
	filename = str(settings.BASE_DIR)+str(obj.file.url)
	response = FileResponse(open(filename, 'rb'))
	return response


def guideline_list(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    today = datetime.now()
    objects = Guidelines.objects.filter(is_active=True).order_by('-datetime')
    lang_data = lang_master(lang)
    paginator = Paginator(objects, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    today = datetime.now().date()
    ip = get_client_ip(request)
    if IpModel.objects.filter(ip=ip).exists():
        if IpModel.objects.filter(ip=ip, datetime__date=today):
            pass
        else:
            IpModel.objects.create(ip=ip)
    else:
        IpModel.objects.create(ip=ip)
    if lang == 'tt':
        titlepage='EDTL.EP - Lista Mata Dalan'
    elif lang == 'pt':
        titlepage='EDTL.EP - Lista Instrucao'
    else:
        titlepage='EDTL.EP - Guideline List'
    try:
        page_description = get_object_or_404(PageManegament, name='guideline', is_active=True)
    except:
        page_description = ''
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,\
                'page_obj':page_obj, 'titlepage':titlepage, 'today': today, 'page_description': page_description
    }
    template = 'inner_page/procurament/guideline.html'
    return render(request, template, context)

def guideline_download(request, hashid):
	obj = get_object_or_404(Guidelines, hashed=hashid)
	filename = str(settings.BASE_DIR)+str(obj.file.url)
	response = FileResponse(open(filename, 'rb'))
	return response


def policy_list(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    today = datetime.now()
    objects = Policy.objects.filter(is_active=True).order_by('-datetime')
    lang_data = lang_master(lang)
    paginator = Paginator(objects, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    today = datetime.now().date()
    ip = get_client_ip(request)
    if IpModel.objects.filter(ip=ip).exists():
        if IpModel.objects.filter(ip=ip, datetime__date=today):
            pass
        else:
            IpModel.objects.create(ip=ip)
    else:
        IpModel.objects.create(ip=ip)
    titlepage = ''
    if lang == 'tt':
        titlepage='EDTL.EP - Lista Regra'
    elif lang == 'pt':
        titlepage='EDTL.EP - Lista Regras'
    else:
        titlepage='EDTL.EP - Policy List'
    try:
        policy_page = get_object_or_404(PageManegament, name='policy', is_active=True)
    except:
        policy_page = ''
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,\
                'page_obj':page_obj, 'titlepage':titlepage, 'today': today, 'policy_page': policy_page
    }
    template = 'inner_page/procurament/policy.html'
    return render(request, template, context)

def policy_download(request, hashid):
	obj = get_object_or_404(Policy, hashed=hashid)
	filename = str(settings.BASE_DIR)+str(obj.file.url)
	response = FileResponse(open(filename, 'rb'))
	return response