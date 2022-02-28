
from django.shortcuts import render, redirect, get_object_or_404
from main.utils_lang import lang_master
from departments.models import Department
from product.models import Product
from event.models import Event
from django.core.paginator import Paginator
from custom.models import IpModel
from main.utils import get_client_ip
from datetime import datetime
def event_list(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    objects = Event.objects.filter(is_active=True)
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
        titlepage='Eventu'
    elif lang == 'pt':
        titlepage='Evento'
    else:
        titlepage='Event'
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products,\
                'page_obj':page_obj, 'lang':lang, 'lang_data': lang_data, 'titlepage':titlepage
    }
    template = 'inner_page/event/list.html'
    return render(request, template, context)


def event_detail(request,lang, hashid):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    objects = get_object_or_404(Event, hashed=hashid)
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
        title2 = f"Eventu: {objects.name_tet}"
        titlepage='Detalla Eventu'
    elif lang == 'pt':
        title2 = f"Evento: {objects.name_por}"
        titlepage='Detalha Evento'
    elif lang == 'en':
        title2 = f"Event: {objects.name_eng}"
        titlepage='Event Detail'
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,\
                'objects': objects, 'title2':title2, 'titlepage':titlepage
    }
    return render(request, 'inner_page/event/detail.html', context)