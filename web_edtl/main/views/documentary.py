from django.shortcuts import render, redirect, get_object_or_404
from main.utils_lang import lang_master
from departments.models import Department
from product.models import Product
from gallery.models import Gallery, GalleryCategory, Album, Video
from django.core.paginator import Paginator
from datetime import datetime
from itertools import chain
from custom.models import Year

def documentary_list(request,lang):
    currentYear = datetime.now()
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    gallery_categories = Department.objects.all()
    album=Album.objects.filter(is_active=True, datetime__year__lt = currentYear.year)
    video=Video.objects.filter(is_active=True, datetime__year__lt = currentYear.year)
    year = Year.objects.all()
    documentary_lists = sorted(
        chain(album, video),
        key=lambda documentary: documentary.datetime, reverse=True
    )
    paginator = Paginator(documentary_lists, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if lang == 'tt':
        legend = "DOCUMENTASAUN"
    elif lang == 'pt':
        legend = "DOCUMENTAÇÃO"
    else :
        legend = "DOCUMENTATION"
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP', \
            'departments':departments,'products': products,'gallery_categories': gallery_categories, 'lang':lang, 'lang_data': lang_data,\
                 'page_obj':page_obj, 'legend': legend, 'year':year
    }
    template = 'inner_page/documentary.html'
    return render(request, template, context)


def documentary_list_filter(request,lang, year):
    get_year = Year.objects.filter(year=year).first()
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    gallery_categories = Department.objects.all()
    try:
        album=Album.objects.filter(is_active=True, datetime__year = get_year.year)
        print(album)
        video=Video.objects.filter(is_active=True, datetime__year = get_year.year)
    except:
        print('Error')
    documentary_lists = sorted(
        chain(album, video),
        key=lambda documentary: documentary.datetime, reverse=True
    )
    year = Year.objects.all()
    paginator = Paginator(documentary_lists, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if lang == 'tt':
        legend = f"DOCUMENTASAUN IHA TINAN {get_year}"
    elif lang == 'pt':
        legend = f"DOCUMENTAÇÃO NO ANO {get_year}"
    else :
        legend = f"DOCUMENTATION IN YEAR {get_year} "
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP', \
            'departments':departments,'products': products,'gallery_categories': gallery_categories, 'lang':lang, 'lang_data': lang_data,\
                 'page_obj':page_obj, 'legend': legend, 'year':year
    }
    template = 'inner_page/documentary.html'
    return render(request, template, context)

def documentary_detail(request,lang, hashid):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    objects = get_object_or_404(Album, hashed=hashid)
    gallery = Gallery.objects.filter(album=objects)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,'objects':objects, 'gallery': gallery
    }
    template = 'inner_page/documentary_detail.html'
    return render(request, template, context)