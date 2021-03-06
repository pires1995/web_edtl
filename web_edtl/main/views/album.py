

from django.shortcuts import render, redirect, get_object_or_404
from main.utils_lang import lang_master
from departments.models import Department
from product.models import Product
from gallery.models import Gallery, GalleryCategory, Album, Video
from django.core.paginator import Paginator
from custom.models import IpModel
from main.utils import get_client_ip
from datetime import datetime

def album_list(request,lang):
    currentYear = datetime.now()
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    gallery_categories = Department.objects.all()
    album = Album.objects.filter(is_active=True,datetime__year=currentYear.year).order_by('-datetime')
    paginator = Paginator(album, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    legend = f"ALBUM {currentYear.year}"
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
        titlepage='EDTL.EP - Lista Album'
    elif lang == 'pt':
        titlepage='EDTL.EP - Lista Album'
    else:
        titlepage='EDTL.EP - Album List'
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,\
                'gallery_categories': gallery_categories, 'titlepage':titlepage, 'page_obj':page_obj, 'legend': legend
    }
    template = 'inner_page/gallery/album_list.html'
    return render(request, template, context)

def album_detail(request,lang, hashid):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    objects = get_object_or_404(Album, hashed=hashid)
    gallery = Gallery.objects.filter(album=objects)
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
        titlepage='EDTL.EP - Detalla Album'
    elif lang == 'pt':
        titlepage='EDTL.EP - Detalha Album'
    else:
        titlepage='EDTL.EP - Album Detail'
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments, 'titlepage':titlepage, 'products': products, 'lang':lang, 'lang_data': lang_data,'objects':objects, 'gallery': gallery
    }
    template = 'inner_page/gallery/album_detail.html'
    return render(request, template, context)

def video_list(request,lang):
    currentYear = datetime.now()
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    gallery_categories = Department.objects.all()
    video = Video.objects.filter(is_active=True,datetime__year=currentYear.year).order_by('-datetime')
    paginator = Paginator(video, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    legend = f"VIDEO {currentYear.year}"
    ip = get_client_ip(request)
    today = datetime.now().date()
    if IpModel.objects.filter(ip=ip).exists():
        if IpModel.objects.filter(ip=ip, datetime__date=today):
            pass
        else:
            IpModel.objects.create(ip=ip)
    else:
        IpModel.objects.create(ip=ip)
    if lang == 'tt':
        titlepage='EDTL.EP - Lista Video'
    elif lang == 'pt':
        titlepage='EDTL.EP - Lista Video'
    else:
        titlepage='EDTL.EP - Video List'
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,\
                'gallery_categories': gallery_categories,'titlepage':titlepage,  'page_obj':page_obj, 'legend': legend
    }
    template = 'inner_page/gallery/video_list.html'
    return render(request, template, context)