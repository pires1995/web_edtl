
from django.shortcuts import render, redirect, get_object_or_404
from main.utils_lang import lang_master
from departments.models import Department
from product.models import Product
from event.models import Event
from django.core.paginator import Paginator

def event_list(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    objects = Event.objects.filter(is_active=True)
    paginator = Paginator(objects, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products,\
                'page_obj':page_obj, 'lang':lang, 'lang_data': lang_data,
    }
    template = 'inner_page/event/list.html'
    return render(request, template, context)


def event_detail(request,lang, hashid):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    objects = get_object_or_404(Event, hashed=hashid)
    if lang == 'tt':
        title2 = f"Eventu: {objects.name_tet}"
    elif lang == 'pt':
        title2 = f"Evento: {objects.name_por}"
    elif lang == 'en':
        title2 = f"Event: {objects.name_eng}"
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,\
                'objects': objects, 'title2':title2
    }
    return render(request, 'inner_page/event/detail.html', context)