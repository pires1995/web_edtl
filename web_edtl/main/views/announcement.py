
from django.shortcuts import render, redirect, get_object_or_404
from main.utils_lang import lang_master
from departments.models import Department
from product.models import Product
from announcement.models import Announcement
from django.core.paginator import Paginator
from custom.models import Year
from custom.models import IpModel
from main.utils import get_client_ip
from django.utils import timezone

def announcement_list(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    objects = Announcement.objects.filter(is_active=True).order_by('-datetime')
    paginator = Paginator(objects, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    today = timezone.now()
    ip = get_client_ip(request)
    if IpModel.objects.filter(ip=ip).exists():
        if IpModel.objects.filter(ip=ip, datetime__contains=today.date()):
            pass
        else:
            IpModel.objects.create(ip=ip)
    else:
        IpModel.objects.create(ip=ip)
    year = Year.objects.all()
    year_data = []
    if lang == 'tt':
        titlepage='EDTL.EP - Lista Anunsiu'
    elif lang == 'pt':
        titlepage='EDTL.EP - Lista Anuncio'
    else:
        titlepage='EDTL.EP - Announcement List'
    for i in year:
        announce = Announcement.objects.filter(is_active=True, datetime__year=i.year).count()
        year_data.append([i, announce])
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,\
                'page_obj': page_obj, 'titlepage':titlepage, 'year':year, 'year_data':year_data
    }
    template = 'inner_page/announcement/list.html'
    return render(request, template, context)

def announcement_list_year(request,lang, year):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    objects = Announcement.objects.filter(is_active=True,datetime__year=year)
    title2=year
    year = Year.objects.all()
    year_data = []
    today = timezone.now()
    ip = get_client_ip(request)
    if IpModel.objects.filter(ip=ip).exists():
        pass
    else:
        IpModel.objects.create(ip=ip)
    if lang == 'tt':
        titlepage='EDTL.EP - Lista Anunsiu'
    elif lang == 'pt':
        titlepage='EDTL.EP - Lista Anuncio'
    else:
        titlepage='EDTL.EP - Announcement List'
    for i in year:
        announce = Announcement.objects.filter(is_active=True, datetime__year=i.year).count()
        year_data.append([i, announce])
    paginator = Paginator(objects, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP', \
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,\
                'page_obj': page_obj, 'titlepage':titlepage, 'year':year, 'year_data':year_data, 'title2':title2
    }
    template = 'inner_page/announcement/list.html'
    return render(request, template, context)

def announcement_detail(request,lang, hashid):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    objects = get_object_or_404(Announcement, hashed=hashid)
    today = timezone.now()
    ip = get_client_ip(request)
    if IpModel.objects.filter(ip=ip).exists():
        pass
    else:
        IpModel.objects.create(ip=ip)
    if lang == 'tt':
        title3 = f"Avisu: {objects.title_tet}"
        titlepage='EDTL.EP - Detalla Anunsiu'
    elif lang == 'pt':
        title3 = f"Aviso: {objects.title_por}"
        titlepage='EDTL.EP - Detalha Anunciuo'
    elif lang == 'en':
        title3 = f"Announcement: {objects.title_eng}"
        titlepage='EDTL.EP - Announcement Detail'
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP','title3':title3,\
            'departments':departments, 'titlepage':titlepage, 'objects': objects, 'lang':lang, 'lang_data': lang_data, 'products':products, 
    }
    template = 'inner_page/announcement/detail.html'
    return render(request, template, context)