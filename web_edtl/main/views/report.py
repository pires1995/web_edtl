from django.shortcuts import render, redirect, get_object_or_404
from main.utils_lang import lang_master
from departments.models import Department, Division
from product.models import Product
from report.models import Report
from django.core.paginator import Paginator
from django.http import FileResponse
from django.conf import settings
from custom.models import IpModel
from main.utils import get_client_ip
from custom.models import Year
from django.utils import timezone


def report_list(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    lang_data = lang_master(lang)
    objects = Report.objects.filter(is_active=True)
    paginator = Paginator(objects, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    year = Year.objects.all()
    year_data = []
    today = timezone.now()
    ip = get_client_ip(request)
    if IpModel.objects.filter(ip=ip).exists():
        if IpModel.objects.filter(ip=ip, datetime__contains=today.date()):
            pass
        else:
            IpModel.objects.create(ip=ip)
    else:
        IpModel.objects.create(ip=ip)
    if lang == 'tt':
        titlepage='EDTL.EP - Lista Relatoriu'
    elif lang == 'pt':
        titlepage='EDTL.EP - Lista Relatorio'
    else:
        titlepage='EDTL.EP - Report List'
    for i in year:
        report = Report.objects.filter(is_active=True, datetime__year=i.year).count()
        year_data.append([i, report])
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP', 'titlepage':titlepage,\
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data, 'page_obj': page_obj, 'year_data':year_data
    }
    template = 'inner_page/report/list.html'
    return render(request, template, context)


def report_detail(request,lang, hashid):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    objects = get_object_or_404(Report, hashed=hashid)
    today = timezone.now()
    ip = get_client_ip(request)
    if IpModel.objects.filter(ip=ip).exists():
        if IpModel.objects.filter(ip=ip, datetime__contains=today.date()):
            pass
        else:
            IpModel.objects.create(ip=ip)
    else:
        IpModel.objects.create(ip=ip)
    if lang == 'tt':
        titlepage='EDTL.EP - Detalla Relatoriu'
    elif lang == 'pt':
        titlepage='EDTL.EP - Detalha Relatorio'
    else:
        titlepage='EDTL.EP - Report Detail'
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP', 'titlepage':titlepage, \
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data, 'objects': objects
    }
    template = 'inner_page/report/detail.html'
    return render(request, template, context)

def report_download(request, hashid):
	obj = get_object_or_404(Report, hashed=hashid)
	filename = str(settings.BASE_DIR)+str(obj.file.url)
	response = FileResponse(open(filename, 'rb'))
	return response

def report_list_year(request,lang, year):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    objects = Report.objects.filter(is_active=True,datetime__year=year)
    title2=year
    year = Year.objects.all()
    year_data = []
    today = timezone.now()
    ip = get_client_ip(request)
    if IpModel.objects.filter(ip=ip).exists():
        if IpModel.objects.filter(ip=ip, datetime__contains=today.date()):
            pass
        else:
            IpModel.objects.create(ip=ip)
    else:
        IpModel.objects.create(ip=ip)
    if lang == 'tt':
        titlepage='EDTL.EP - Lista Relatoriu'
    elif lang == 'pt':
        titlepage='EDTL.EP - Lista Relatorio'
    else:
        titlepage='EDTL.EP - Report List'
    for i in year:
        announce = Report.objects.filter(is_active=True, datetime__year=i.year).count()
        year_data.append([i, announce])
    paginator = Paginator(objects, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP', \
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,\
                'page_obj': page_obj, 'titlepage':titlepage, 'year':year, 'year_data':year_data, 'title2':title2
    }
    template = 'inner_page/report/list.html'
    return render(request, template, context)