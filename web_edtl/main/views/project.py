

from django.shortcuts import render, get_object_or_404
from main.utils_lang import lang_master
from departments.models import Department
from product.models import Product
from project.models import Project, ProjectBudget, ProjectCategory, ProjectLocation, ProjectStatus
from django.core.paginator import Paginator
from custom.models import IpModel
from main.utils import get_client_ip
from datetime import datetime

def project_ongoing_list(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    objects = Project.objects.filter(is_active=True, project_status_id=2).order_by('-datetime')
    paginator = Paginator(objects, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    today = datetime.now().date()
    ip = get_client_ip(request)
    if IpModel.objects.filter(ip=ip).exists():
        if IpModel.objects.filter(ip=ip, datetime__contains=today):
            pass
        else:
            IpModel.objects.create(ip=ip)
    else:
        IpModel.objects.create(ip=ip)
    if lang == 'tt':
        titlepage='EDTL.EP - Lista Projetu'
    elif lang == 'pt':
        titlepage='EDTL.EP - Lista Projeto'
    else:
        titlepage='EDTL.EP - Project List'
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,
            'page_obj': page_obj, 'titlepage':titlepage
    }
    template = 'inner_page/project/ongoing.html'
    return render(request, template, context)

def project_ongoing_detail(request,lang, hashid):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    today = datetime.now().date()
    ip = get_client_ip(request)
    if IpModel.objects.filter(ip=ip).exists():
        if IpModel.objects.filter(ip=ip, datetime__contains=today):
            pass
        else:
            IpModel.objects.create(ip=ip)
    else:
        IpModel.objects.create(ip=ip)
    if lang == 'tt':
        titlepage='EDTL.EP - Detalla Projetu'
    elif lang == 'pt':
        titlepage='EDTL.EP - Detalha Projeto'
    else:
        titlepage='EDTL.EP - Project Detail'
    location = None
    budget = None
    try:
        objects = get_object_or_404(Project, hashed=hashid)
        budget = get_object_or_404(ProjectBudget, project=objects)
        location = get_object_or_404(ProjectLocation, project=objects)
    except:
        objects = get_object_or_404(Project, hashed=hashid)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP', \
            'departments':departments, 'products': products, 'lang':lang, 'lang_data': lang_data,\
                'objects': objects, 'titlepage':titlepage, 'location': location, 'budget':budget
    }
    template = 'inner_page/project/ongoing_detail.html'
    return render(request, template, context)

def project_new_list(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    objects = Project.objects.filter(is_active=True, project_status_id=2).order_by('-datetime')
    paginator = Paginator(objects, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    today = datetime.now().date()
    ip = get_client_ip(request)
    if IpModel.objects.filter(ip=ip).exists():
        if IpModel.objects.filter(ip=ip, datetime__contains=today):
            pass
        else:
            IpModel.objects.create(ip=ip)
    else:
        IpModel.objects.create(ip=ip)
    if lang == 'tt':
        titlepage='EDTL.EP - Lista Projetu Foun'
    elif lang == 'pt':
        titlepage='EDTL.EP - Lista Novo Projeto'
    else:
        titlepage='EDTL.EP - Up Coming Project'
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP', \
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,\
                'page_obj': page_obj, 'titlepage':titlepage
    }
    template = 'inner_page/project/new.html'
    return render(request, template, context)

def project_new_detail(request,lang, hashid):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    today = datetime.now().date()
    ip = get_client_ip(request)
    if IpModel.objects.filter(ip=ip).exists():
        if IpModel.objects.filter(ip=ip, datetime__contains=today):
            pass
        else:
            IpModel.objects.create(ip=ip)
    else:
        IpModel.objects.create(ip=ip)
    if lang == 'tt':
        titlepage='EDTL.EP - Detalla Projetu'
    elif lang == 'pt':
        titlepage='EDTL.EP - Detalha Projeto'
    else:
        titlepage='EDTL.EP - Project Detail'
    location = None
    budget = None
    try:
        objects = get_object_or_404(Project, hashed=hashid)
        budget = get_object_or_404(ProjectBudget, project=objects)
        location = get_object_or_404(ProjectLocation, project=objects)
    except:
        objects = get_object_or_404(Project, hashed=hashid)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP', \
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,\
                'objects': objects, 'titlepage':titlepage, 'location': location, 'budget':budget
    }
    template = 'inner_page/project/new_detail.html'
    return render(request, template, context)
