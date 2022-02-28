from django.shortcuts import render, redirect, get_object_or_404
from news.forms import NewsUserSignUpForm
from news.models import NewsUser
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template
from main.utils_lang import lang_master
from profiles.models import Position, About, Service, Deliverasaun
from departments.models import Department
from product.models import Product
from pagemanegament.models import PageManegament
from custom.models import IpModel
from main.utils import get_client_ip
from django.core.paginator import Paginator
from django.utils import timezone

def who_we_are(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    objects = About.objects.all().first()
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
        titlepage='Se Mak Ami'
        legend = 'SE MAK AMI'
    elif lang == 'pt':
        titlepage='Quem Nos Somos'
        legend = 'QUEM NÓS SOMOS'
    else:
        titlepage='Who We Are'
        legend = 'WHO WE ARE'
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en', 'legend': legend, \
        'objects':objects, 'titlepage':titlepage, 'departments':departments,'products': products,'title': 'EDTL, EP', 'lang':lang, 'lang_data': lang_data,
    }
    template = 'inner_page/about/who_we_are.html'
    return render(request, template, context)

def what_we_do(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    objects = Service.objects.filter(is_active=True)
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
        titlepage='Ami nia Servisu'
    elif lang == 'pt':
        titlepage='What We Do'
    else:
        titlepage='What We Do'
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','titlepage':titlepage, \
            'departments':departments,'products': products,'title': 'EDTL, EP', 'lang':lang, 'lang_data': lang_data, 'objects':objects
    }
    template = 'inner_page/about/what_we_do.html'
    return render(request, template, context)

def board_profile(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    boardmembers = Position.objects.filter(group='Board Member')
    departments_board = Position.objects.filter(group='Department')
    divisions_board = Position.objects.filter(group='Division')
    gabinete = Position.objects.filter(group='Gabineti Apoiu Servisu')
    pmu = Position.objects.filter(group='Project Management Unit')
    auditoria = Position.objects.filter(group='Auditoria')
    today = timezone.now()
    deliverasaun = Deliverasaun.objects.filter(is_active=True).order_by('datetime')[:10]
    ip = get_client_ip(request)
    if IpModel.objects.filter(ip=ip).exists():
        if IpModel.objects.filter(ip=ip, datetime__contains=today.date()):
            pass
        else:
            IpModel.objects.create(ip=ip)
    else:
        IpModel.objects.create(ip=ip)
    if lang == 'tt':
        titlepage='Perfil Membru'
    elif lang == 'pt':
        titlepage='Perfil Membro'
    else:
        titlepage='Board Director Profile'
    try:
        page_description = get_object_or_404(PageManegament, name='board-director', is_active=True)
    except:
        page_description = ''
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','titlepage':titlepage,\
            'departments':departments,'products': products,'title': 'EDTL, EP', 'lang':lang, 'lang_data': lang_data,
        'boardmembers': boardmembers, 'departments_board':departments_board,\
            'divisions_board':divisions_board, 'page_description': page_description,\
                'gabinete':gabinete, 'pmu':pmu, 'auditoria':auditoria, 'deliverasaun':deliverasaun
    }
    template = 'inner_page/about/board_profile.html'
    return render(request, template, context)

def cabinet_profile(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    gabinete = Position.objects.filter(group='Gabineti Apoiu Servisu')
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
        titlepage='Perfil Gabinete'
    elif lang == 'pt':
        titlepage='Perfil Gabinete'
    else:
        titlepage='Profile Cabinet'
    try:
        page_description = get_object_or_404(PageManegament, name='board-cabinet', is_active=True)
    except:
        page_description = ''
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','titlepage':titlepage,\
            'departments':departments,'products': products,'title': 'EDTL, EP', 'lang':lang, 'lang_data': lang_data,\
            'page_description': page_description,\
                'gabinete':gabinete, 
    }
    template = 'inner_page/about/cabinet_profile.html'
    return render(request, template, context)


def pmu_profile(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    pmu = Position.objects.filter(group='Project Management Unit')
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
        titlepage='Perfil PMU'
    elif lang == 'pt':
        titlepage='Perfil PMU'
    else:
        titlepage='PMU Profile'
    try:
        page_description = get_object_or_404(PageManegament, name='board-pmu', is_active=True)
    except:
        page_description = ''
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','titlepage':titlepage,\
            'departments':departments,'products': products,'title': 'EDTL, EP', 'lang':lang, 'lang_data': lang_data,'page_description': page_description,\
              'pmu':pmu,
    }
    template = 'inner_page/about/pmu_profile.html'
    return render(request, template, context)

def audit_profile(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    auditoria = Position.objects.filter(group='Auditoria')
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
        titlepage='Perfil Auditoria'
    elif lang == 'pt':
        titlepage='Perfil Auditoria'
    else:
        titlepage='Audit Profile'
    try:
        page_description = get_object_or_404(PageManegament, name='board-auditoria', is_active=True)
    except:
        page_description = ''
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','titlepage':titlepage,\
            'departments':departments,'products': products,'title': 'EDTL, EP', 'lang':lang, 'lang_data': lang_data,'page_description': page_description,\
              'auditoria':auditoria,
    }
    template = 'inner_page/about/audit_profile.html'
    return render(request, template, context)


def board_detail(request, hashid, lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    objects = get_object_or_404(Position, hashed=hashid)
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
        titlepage='Detalla Membru'
    elif lang == 'pt':
        titlepage='Detalha Membro'
    else:
        titlepage='Member Detail'
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en',\
            'departments':departments,'products': products,'title': 'EDTL, EP', 'lang':lang,
            'objects': objects, 'lang_data': lang_data, 'titlepage':titlepage
    }
    template = 'inner_page/about/board_detail.html'
    return render(request, template, context)

def deliverasaun_list(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    objects = Deliverasaun.objects.filter(is_active=True)
    paginator = Paginator(objects, 5)
    page_number = request.GET.get('page')
    today = timezone.now()
    ip = get_client_ip(request)
    if IpModel.objects.filter(ip=ip).exists():
        if IpModel.objects.filter(ip=ip, datetime__contains=today.date()):
            pass
        else:
            IpModel.objects.create(ip=ip)
    else:
        IpModel.objects.create(ip=ip)
    page_obj = paginator.get_page(page_number)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products,\
                'page_obj':page_obj, 'lang':lang, 'lang_data': lang_data,
    }
    template = 'inner_page/about/deliverasaun_list.html'
    return render(request, template, context)


def deliverasaun_detail(request,lang,year,month,day,hashid):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    objects = get_object_or_404(Deliverasaun, hashed=hashid)
    today = timezone.now()
    ip = get_client_ip(request)
    if IpModel.objects.filter(ip=ip).exists():
        if IpModel.objects.filter(ip=ip, datetime__contains=today.date()):
            pass
        else:
            IpModel.objects.create(ip=ip)
    else:
        IpModel.objects.create(ip=ip)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP', \
            'departments':departments,'products': products,'lang':lang, 'lang_data': lang_data, 'objects':objects
    }
    template = 'inner_page/about/deliverasaun_detail.html'
    return render(request, template, context)

def executive_directors(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    objects = Position.objects.filter(group='Executive Directors')
    paginator = Paginator(objects, 5)
    page_number = request.GET.get('page')
    today = timezone.now()
    ip = get_client_ip(request)
    if IpModel.objects.filter(ip=ip).exists():
        if IpModel.objects.filter(ip=ip, datetime__contains=today.date()):
            pass
        else:
            IpModel.objects.create(ip=ip)
    else:
        IpModel.objects.create(ip=ip)
    page_obj = paginator.get_page(page_number)
    try:
        page_description = get_object_or_404(PageManegament, name='executive', is_active=True)
    except:
        page_description = ''
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products,\
                'page_obj':page_obj, 'lang':lang, 'lang_data': lang_data, 'page_description':page_description
    }
    template = 'inner_page/about/executive_directors.html'
    return render(request, template, context)