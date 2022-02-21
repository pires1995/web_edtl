
from django.shortcuts import render, redirect, get_object_or_404
from main.utils_lang import lang_master
from departments.models import Department
from product.models import Product
from announcement.models import Announcement
from django.core.paginator import Paginator
from custom.models import Year


def announcement_list(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    objects = Announcement.objects.filter(is_active=True).order_by('-datetime')
    paginator = Paginator(objects, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    year = Year.objects.all()
    year_data = []
    for i in year:
        announce = Announcement.objects.filter(is_active=True, datetime__year=i.year).count()
        year_data.append([i, announce])
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,\
                'page_obj': page_obj, 'year':year, 'year_data':year_data
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
    for i in year:
        announce = Announcement.objects.filter(is_active=True, datetime__year=i.year).count()
        year_data.append([i, announce])
    paginator = Paginator(objects, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP', \
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,\
                'page_obj': page_obj, 'year':year, 'year_data':year_data, 'title2':title2
    }
    template = 'inner_page/announcement/list.html'
    return render(request, template, context)

def announcement_detail(request,lang, hashid):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    objects = get_object_or_404(Announcement, hashed=hashid)
    if lang == 'tt':
        title3 = f"Avisu: {objects.title_tet}"
    elif lang == 'pt':
        title3 = f"Aviso: {objects.title_por}"
    elif lang == 'en':
        title3 = f"Announcement: {objects.title_eng}"
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP','title3':title3,\
            'departments':departments,'objects': objects, 'lang':lang, 'lang_data': lang_data, 'products':products, 
    }
    template = 'inner_page/announcement/detail.html'
    return render(request, template, context)