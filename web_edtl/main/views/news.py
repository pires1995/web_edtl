from unicodedata import category
from django.shortcuts import render, redirect, get_object_or_404
from main.utils_lang import lang_master
from news.models import News, NewsCategory, NewsImage, NewsComment
from departments.models import Department
from product.models import Product
from news.models import News
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Count, Q
from news.forms import NewsCommentForm
from main.utils import getnewid
from custom.models import IpModel, Year
from main.forms import SubscribeForm
from news.models import News, NewsUser, SubscribeChoice
from main.utils import get_client_ip
from datetime import datetime
def news_list(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    years = Year.objects.all()
    today = datetime.now().date()
    ip = get_client_ip(request)
    if IpModel.objects.filter(ip=ip).exists():
        if IpModel.objects.filter(ip=ip, datetime__contains=today):
            pass
        else:
            IpModel.objects.create(ip=ip)
    else:
        IpModel.objects.create(ip=ip)
    if lang == "tt":
        queryset_list = News.objects.filter(is_active=True,is_approved=True, language="Tetum").all().order_by('-date_posted')
        news_category = NewsCategory.objects.all()
        total = queryset_list.count()
        pagetitle='Lista Notisia'
        data = []
        year_data = []
        for n in news_category:
            news = News.objects.filter(is_active=True,is_approved=True,news_category=n, language="Tetum").count()
            data.append([n.name_tet,news,n.hashed])
        
        for year in years:
            news = News.objects.filter(is_active=True,is_approved=True,entered_date__year=year.year, language="Tetum").count()
            year_data.append([year.year,news])

        legend = "NOTICIA"
        search = "Buka Noticia"
    elif lang == "pt":
        queryset_list = News.objects.filter(is_active=True,is_approved=True, language="Portugues").all().order_by('-date_posted')
        news_category = NewsCategory.objects.all()
        total = queryset_list.count()
        pagetitle='Lista Noticia'
        data = []
        year_data = []
        for n in news_category:
            news = News.objects.filter(is_active=True,is_approved=True,news_category=n, language="Portugues").count()
            data.append([n.name_por,news,n.hashed])
        for year in years:
            news = News.objects.filter(is_active=True,is_approved=True,entered_date__year=year.year, language="Portugues").count()
            year_data.append([year.year,news])
        legend = "NOTÍCIAS"
        search = "Procurar Notícia"
    else:
        queryset_list = News.objects.filter(is_active=True,is_approved=True, language="English").all().order_by('-date_posted')
        news_category = NewsCategory.objects.all()
        total = queryset_list.count()
        pagetitle='News List'
        data = []
        year_data = []
        for n in news_category:
            news = News.objects.filter(is_active=True,is_approved=True,news_category=n, language="English").count()
            data.append([n.name_eng,news,n.hashed])
        for year in years:
            news = News.objects.filter(is_active=True,is_approved=True,entered_date__year=year.year, language="English").count()
            year_data.append([year.year,news])
        legend = "NEWS"
        search = "Search for News"
    query = request.GET.get("q")    
    if query:
        queryset_list = queryset_list.filter(
        (Q(title__icontains=query))).distinct()
    else:
        queryset_list = queryset_list
    lang_data = lang_master(lang)
    paginator = Paginator(queryset_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    form =  SubscribeForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                check_email = NewsUser.objects.get(email=email)
                if check_email:
                    messages.error(request,'Email Already Exists')
                    return redirect('redirect-home')
            except:
                    subscribe = SubscribeChoice.objects.all()
                    usersub = NewsUser.objects.create(email=email)
                    for i in subscribe:
                        usersub.choices.add(i)
                    messages.success(request,'Please Confirm Email')
                    return redirect('redirect-home')
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,\
                'news_cat_count': data, 'total': total, 'year_data':year_data,
             'queryset_list': queryset_list, 'legend':legend, 'search':search, 'page_obj':page_obj, 'titlepage':pagetitle
    }
    template = 'inner_page/news/news_list.html'
    return render(request, template, context)

def news_list_category(request,lang, hashid):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    years = Year.objects.all()
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
    if lang == "tt":
        queryset_list = News.objects.filter(is_active=True,is_approved=True, language="Tetum",news_category__hashed=hashid).all().order_by('-date_posted')
        cat = get_object_or_404(NewsCategory, hashed=hashid)
        total = queryset_list.count()
        title2 = cat.name_tet
        news_category = NewsCategory.objects.all()
        titlepage='Lista Notisia'
        data = []
        year_data = []
        for n in news_category:
            news = News.objects.filter(is_active=True,is_approved=True,news_category=n, language="Tetum").count()
            data.append([n.name_tet,news,n.hashed])
        for year in years:
            news = News.objects.filter(is_active=True,is_approved=True,entered_date__year=year.year, language="Tetum").count()
            year_data.append([year.year,news])
        legend = "NOTICIA"
        
        search = "Buka Noticia"
    elif lang == "pt":
        queryset_list = News.objects.filter(is_active=True,is_approved=True, language="Portugues",news_category__hashed=hashid).all().order_by('-date_posted')
        news_category = NewsCategory.objects.all()
        total = queryset_list.count()
        titlepage='Lista Noticia'
        cat = get_object_or_404(NewsCategory, hashed=hashid)
        title2 = cat.name_por
        data = []
        year_data = []
        for n in news_category:
            news = News.objects.filter(is_active=True,is_approved=True,news_category=n, language="Portugues").count()
            data.append([n.name_por,news,n.hashed])
        for year in years:
            news = News.objects.filter(is_active=True,is_approved=True,entered_date__year=year.year, language="Portugues").count()
            year_data.append([year.year,news])
        legend = "NOTÍCIAS"
        
        search = "Procurar Notícia"
    else:
        queryset_list = News.objects.filter(is_active=True,is_approved=True, language="English",news_category__hashed=hashid).all().order_by('-date_posted')
        news_category = NewsCategory.objects.all()
        total = queryset_list.count()
        cat = get_object_or_404(NewsCategory, hashed=hashid)
        titlepage='Lista Noticia'
        title2 = cat.name_eng
        data = []
        year_data = []
        for n in news_category:
            news = News.objects.filter(is_active=True,is_approved=True,news_category=n, language="English").count()
            data.append([n.name_eng,news,n.hashed])
        for year in years:
            news = News.objects.filter(is_active=True,is_approved=True,entered_date__year=year.year, language="English").count()
            year_data.append([year.year,news])
        legend = "NEWS"
        
        search = "Search for News"
    lang_data = lang_master(lang)
    paginator = Paginator(queryset_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,\
                'news_cat_count': data, 'total': total, 'year_data':year_data,
            'legend':legend, 'search':search, 'page_obj':page_obj, 'title2': title2, 'titlepage':titlepage
    }
    template = 'inner_page/news/news_list.html'
    return render(request, template, context)

def news_list_year(request, lang, year):
    lang_data = lang_master(lang)
    years = Year.objects.all()
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
    if lang == "tt":
        queryset_list = News.objects.filter(is_active=True,is_approved=True, language="Tetum",entered_date__year=year).all().order_by('-date_posted')
        year = get_object_or_404(Year, year=year)
        title2 = year
        total = queryset_list.count()
        news_category = NewsCategory.objects.all()
        titlepage='Lista Notisia'
        data = []
        year_data = []
        for n in news_category:
            news = News.objects.filter(is_active=True,is_approved=True,news_category=n, language="Tetum").count()
            data.append([n.name_tet,news,n.hashed])
        legend = "NOTICIA"
        for year in years:
            news = News.objects.filter(is_active=True,is_approved=True,entered_date__year=year.year, language="Tetum").count()
            year_data.append([year.year,news])
        search = "Buka Noticia"
    elif lang == "pt":
        queryset_list = News.objects.filter(is_active=True,is_approved=True, language="Portugues",entered_date__year=year).all().order_by('-date_posted')
        news_category = NewsCategory.objects.all()
        total = queryset_list.count()
        year = get_object_or_404(Year, year=year)
        titlepage='Lista Noticia'
        title2 = year
        data = []
        year_data = []
        for n in news_category:
            news = News.objects.filter(is_active=True,is_approved=True,news_category=n, language="Portugues").count()
            data.append([n.name_por,news,n.hashed])
        for year in years:
            news = News.objects.filter(is_active=True,is_approved=True,entered_date__year=year.year, language="Portugues").count()
            year_data.append([year.year,news])
        legend = "NOTÍCIAS"
        
        search = "Procurar Notícia"
    else:
        queryset_list = News.objects.filter(is_active=True,is_approved=True, language="English",entered_date__year=year).all().order_by('-date_posted')
        news_category = NewsCategory.objects.all()
        total = queryset_list.count()
        year = get_object_or_404(Year, year=year)
        titlepage='News List'
        title2 = year
        data = []
        year_data = []
        for n in news_category:
            news = News.objects.filter(is_active=True,is_approved=True,news_category=n, language="English").count()
            data.append([n.name_eng,news,n.hashed])
        for year in years:
            news = News.objects.filter(is_active=True,is_approved=True,entered_date__year=year.year, language="English").count()
            year_data.append([year.year,news])
        legend = "NEWS"
        
        search = "Search for News"
    lang_data = lang_master(lang)
    paginator = Paginator(queryset_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,\
                'news_cat_count': data, 'total': total, 'year_data':year_data,
            'legend':legend, 'search':search, 'page_obj':page_obj, 'title2': title2, 'titlepage':titlepage
    }
    template = 'inner_page/news/news_list.html'
    return render(request, template, context)




def news_detail(request,lang,year, month, hashid, titleseo):
    ip = get_client_ip(request)
    if lang == "tt":
        if IpModel.objects.filter(ip=ip).exists():
            titlepage = 'Detalla Notisia'
            objects = get_object_or_404(News, hashed=hashid, language="Tetum")
            objects.views.add(IpModel.objects.filter(ip=ip).last())
            breakcumb = 'Lista Notisia'
            legend = "Detalha"
        else:
            IpModel.objects.create(ip=ip)
            titlepage = 'Detalla Notisia'
            objects = get_object_or_404(News, hashed=hashid, language="Tetum")
            objects.views.add(IpModel.objects.filter(ip=ip).last())
            breakcumb = 'Lista Notisia'
            legend = "Detalha"
    elif lang == "pt":
        if IpModel.objects.filter(ip=ip).exists():
            titlepage = 'Detalha Noticia'
            objects = get_object_or_404(News, hashed=hashid, language="Portugues")
            objects.views.add(IpModel.objects.filter(ip=ip).last())
            breakcumb = 'Lista Notisia'
            legend = "Detalha"
        else:
            IpModel.objects.create(ip=ip)
            titlepage = 'Detalha Noticia'
            objects = get_object_or_404(News, hashed=hashid, language="Portugues")
            objects.views.add(IpModel.objects.filter(ip=ip).last())
            breakcumb = 'Lista Notisia'
            legend = "Detalha"

    else:
        if IpModel.objects.filter(ip=ip).exists():
            titlepage = 'Detail'
            objects = get_object_or_404(News, hashed=hashid, language="English")
            objects.views.add(IpModel.objects.filter(ip=ip).last())
            breakcumb = 'Lista Notisia'
            legend = "News Detail"
        else:
            IpModel.objects.create(ip=ip)
            titlepage = 'Detail'
            objects = get_object_or_404(News, hashed=hashid, language="English")
            objects.views.add(IpModel.objects.filter(ip=ip).last())
            breakcumb = 'Lista Notisia'
            legend = "News Detail"
    lang_data = lang_master(lang)
    images = NewsImage.objects.filter(news=objects)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    comments = NewsComment.objects.filter(news__hashed=hashid, is_approved=True)
    if request.method == 'POST':
        newid, new_hashed = getnewid(NewsComment)
        form = NewsCommentForm(request.POST)
        news = get_object_or_404(News, hashed=hashid)
        if form.is_valid():
            admin_email = form.cleaned_data.get('email')
            if admin_email == 'edtlep@gmail.com':
                instance2 = form.save(commit=False)
                instance2.id = newid
                instance2.hashed = new_hashed
                instance2.news = news
                instance2.name = 'Admin EDTL,EP'
                instance2.is_admin = True
                instance2.is_approved = True
                instance2.save()
                messages.success(request, 'Successfully Submit Your Comment')
                return redirect('news-detail',lang, year, month, hashid, titleseo )
            else:
                instance = form.save(commit=False)
                instance.news = news
                instance.id = newid
                instance.hashed = new_hashed
                instance.save()
                messages.success(request, 'Successfully Submit Your Comment')
                return redirect('news-detail',lang, year, month, hashid, titleseo )
    else:
        form = NewsCommentForm()

    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP','products': products,\
        'departments':departments, 'lang':lang, 'lang_data': lang_data, \
        'objects': objects, 'legend':legend, 'images': images, 'breakcumb':breakcumb, \
            'form':form, 'comments':comments, 'titlepage':titlepage
    }
    template = 'inner_page/news/news_detail.html'
    return render(request, template, context)
