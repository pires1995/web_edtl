from unicodedata import category
from django.shortcuts import render, redirect, get_object_or_404
from main.utils_lang import lang_master
from news.models import News, NewsCategory, NewsImage
from departments.models import Department
from product.models import Product
from news.models import News
from django.core.paginator import Paginator
from django.db.models import Count, Q

def news_list(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    if lang == "tt":
        news_group = News.objects.filter(is_approved=True,language="Tetum").distinct().values('date_posted__year').all()
        queryset_list = News.objects.filter(is_active=True,is_approved=True, language="Tetum").all().order_by('-date_posted')
        news_category = NewsCategory.objects.all()
        data = []
        for n in news_category:
            news = News.objects.filter(is_active=True,is_approved=True,news_category=n, language="Tetum").count()
            data.append([n.name_tet,news])
        legend = "NOTICIA"
        search = "Buka Noticia"
    elif lang == "pt":
        news_group = News.objects.filter(is_approved=True,language="Portugues").distinct().values('date_posted__year').all()
        queryset_list = News.objects.filter(is_active=True,is_approved=True, language="Portugues").all().order_by('-date_posted')
        news_category = NewsCategory.objects.all()
        data = []
        for n in news_category:
            news = News.objects.filter(is_active=True,is_approved=True,news_category=n, language="Portugues").count()
            data.append([n.name_por,news])
        legend = "NOTÍCIAS"
        search = "Procurar Notícia"
    else:
        news_group = News.objects.filter(is_approved=True,language="English").distinct().values('entered_date__year').all()
        queryset_list = News.objects.filter(is_active=True,is_approved=True, language="English").all().order_by('-date_posted')
        news_category = NewsCategory.objects.all()
        data = []
        for n in news_category:
            news = News.objects.filter(is_active=True,is_approved=True,news_category=n, language="English").count()
            data.append([n.name_eng,news])
        legend = "NEWS"
        search = "Search for News"
    lang_data = lang_master(lang)
    paginator = Paginator(queryset_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,\
                'news_cat_count': data,
            'news_group':news_group, 'queryset_list': queryset_list, 'legend':legend, 'search':search, 'page_obj':page_obj
    }
    template = 'inner_page/news/news_list.html'
    return render(request, template, context)


def news_detail(request,lang,year, month, hashid, titleseo):
    if lang == "tt":
        objects = get_object_or_404(News, hashed=hashid, language="Tetum")
        breakcumb = 'Lista Notisia'
        legend = "Detalha"
    elif lang == "pt":
        objects = get_object_or_404(News, hashed=hashid, language="Portugues")
        breakcumb = 'Lista Notícia'
        legend = "Detalha"
    else:
        objects = get_object_or_404(News, hashed=hashid, language="English")
        breakcumb = 'News List'
        legend = "Detail"
    lang_data = lang_master(lang)
    images = NewsImage.objects.filter(news=objects)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)

    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP','products': products,\
        'departments':departments, 'lang':lang, 'lang_data': lang_data, \
        'objects': objects, 'legend':legend, 'images': images, 'breakcumb':breakcumb
    }
    template = 'inner_page/news/news_detail.html'
    return render(request, template, context)
