
from random import choices
from django.shortcuts import render, redirect, get_object_or_404
from news.forms import NewsUserSignUpForm
from news.models import NewsUser, SubscribeChoice
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template
from main.utils_lang import lang_master
from news.models import News
from departments.models import Department, Division
from product.models import Product
from gallery.models import GalleryCategory, Banner
from news.models import News
from faq.models import Faq
from django.core.paginator import Paginator
from django.conf import settings
from main.forms import SubscribeForm
from news.tasks import new_subs
import re
from procurament.models import Tender
from datetime import datetime, timedelta
from recruitment.models import Vacancy
from django.http import HttpResponse
from custom.models import IpModel
from main.utils import get_client_ip
from django.utils import timezone
from django.db.models import Q
from event.models import Event
from announcement.models import Announcement
from itertools import chain
def home(request, lang):
    
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    banners = Banner.objects.filter(is_active=True).order_by('-datetime')[:5]
    news_main = News.objects.filter(is_active=True, is_approved=True, language="English").last()
    news_recent = News.objects.filter(is_active=True, is_approved=True, language="English").order_by('-approved_date')[1:4]
    faq_home = Faq.objects.filter(is_active=True, is_homepage=True)
    vacancy_marquee = Vacancy.objects.filter(is_active=True, end_period__gte = datetime.now().date())[:3]
    tender_marquee = Tender.objects.filter(is_active=True, end_period__gte = datetime.now().date())[:3]
    
    visitors = IpModel.objects.all().count()
    today = datetime.now().date()
    last_month =  today - timedelta(days=30)
    yesterday =  today - timedelta(days=1)
    last_month_visitor = IpModel.objects.filter(datetime__range=(last_month,today,)).count()
    yesterday_visitor = IpModel.objects.filter(datetime__contains=yesterday).count()
    today_visitor = IpModel.objects.filter(datetime__contains=today).count()
    ip = get_client_ip(request)
    if IpModel.objects.filter(ip=ip).exists():
        if IpModel.objects.filter(ip=ip, datetime__contains=today):
            pass
        else:
            IpModel.objects.create(ip=ip)
    else:
        IpModel.objects.create(ip=ip)
    form =  SubscribeForm(request.POST or None)
    titlepage = 'Home'
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
                set_name = usersub.email
                set_name2 = re.split(r'[@.]', set_name)
                domain = request.get_host() + f'/email-confirmation/{usersub.date_created.day}/{set_name2[0]}/{usersub.date_created.minute}/{usersub.hashed}'

                for i in subscribe:
                    usersub.choices.add(i)
                new_subs.delay(usersub.email, set_name2[0], domain)
                messages.success(request,'Please Confirm Email')
                return redirect('redirect-home')

    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP','lang': lang, 'lang_data': lang_data,\
            'page': 'varanda', 'departments': departments, 'products': products, 'banners':banners, 'visitors':visitors, 'last_month_visitor':last_month_visitor,\
                'yesterday_visitor':yesterday_visitor, 'today_visitor':today_visitor,
            'news_main': news_main, 'vacancy_event':vacancy_marquee, 'tender_marquee':tender_marquee, 'news_recent':news_recent, 'faq_home':faq_home, 'titlepage':titlepage
    }
    template = 'main/home.html'
    return render(request, template, context)


def inicio(request, lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    banners = Banner.objects.filter(is_active=True)
    news_main = News.objects.filter(is_active=True, is_approved=True, language="Portugues").last()
    news_recent = News.objects.filter(is_active=True, is_approved=True, language="Portugues").order_by('-approved_date')[1:4]
    faq_home = Faq.objects.filter(is_active=True, is_homepage=True)
    today = datetime.now().date()
    last_month =  today - timedelta(days=30)
    yesterday =  today - timedelta(days=1)
    last_month_visitor = IpModel.objects.filter(datetime__range=(last_month,today,)).count()
    yesterday_visitor = IpModel.objects.filter(datetime__contains=yesterday).count()
    today_visitor = IpModel.objects.filter(datetime__contains=today).count()
    ip = get_client_ip(request)
    if IpModel.objects.filter(ip=ip).exists():
        if IpModel.objects.filter(ip=ip, datetime__contains=today):
            pass
        else:
            IpModel.objects.create(ip=ip)
    else:
        IpModel.objects.create(ip=ip)
    visitors = IpModel.objects.all().count()
    form =  SubscribeForm(request.POST or None)
    titlepage = 'Inicio'
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
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP','lang': lang, 'lang_data': lang_data,\
            'page': 'varanda','visitors':visitors, 'last_month_visitor':last_month_visitor,\
                'yesterday_visitor':yesterday_visitor, 'today_visitor':today_visitor, 'departments': departments, 'products': products, 'banners':banners, 
            'news_main': news_main, 'news_recent':news_recent, 'faq_home':faq_home, 'titlepage':titlepage
    }
    template = 'main/inicio.html'
    return render(request, template, context)

def varanda(request, lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    banners = Banner.objects.filter(is_active=True)
    news_main = News.objects.filter(is_active=True, is_approved=True, language="Tetum").last()
    news_recent = News.objects.filter(is_active=True, is_approved=True, language="Tetum").order_by('-approved_date')[1:4]
    faq_home = Faq.objects.filter(is_active=True, is_homepage=True)
    visitors = IpModel.objects.all().count()
    today = datetime.now().date()
    last_month =  today - timedelta(days=30)
    yesterday =  today - timedelta(days=1)
    last_month_visitor = IpModel.objects.filter(datetime__range=(last_month,today,)).count()
    yesterday_visitor = IpModel.objects.filter(datetime__contains=yesterday).count()
    today_visitor = IpModel.objects.filter(datetime__contains=today).count()
    ip = get_client_ip(request)
    if IpModel.objects.filter(ip=ip).exists():
        if IpModel.objects.filter(ip=ip, datetime__contains=today):
            pass
        else:
            IpModel.objects.create(ip=ip)
    else:
        IpModel.objects.create(ip=ip)
    form =  SubscribeForm(request.POST or None)
    titlepage = 'Varanda'
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
                    set_name = usersub.email
                    set_name2 = re.split(r'[@.]', set_name)
                    for i in subscribe:
                        usersub.choices.add(i)
                    new_subs.delay(usersub.email, set_name2[0], 'Teste')
                    messages.success(request,'Please Confirm Email')
                    return redirect('redirect-home')
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP','lang': lang, 'lang_data': lang_data,\
            'page': 'varanda', 'visitors':visitors, 'last_month_visitor':last_month_visitor,\
               'yesterday_visitor':yesterday_visitor, 'today_visitor':today_visitor, 'departments': departments, 'products': products, 'banners':banners, 
            'news_main': news_main, 'news_recent':news_recent, 'faq_home':faq_home, 'titlepage':titlepage
    }
    template = 'main/home.html'
    return render(request, template, context)

def email_confirmation(request, day,name, minute, hashid):
    instance = get_object_or_404(NewsUser, hashed=hashid)
    instance.is_active = True
    instance.save()
    messages.success(request,'Email has been Confirm')
    return redirect('redirect-home')


def department(request,lang):
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
    titlepage = ''
    if lang == 'tt':
        titlepage='EDTL.EP - Detalla Departamentu'
    elif lang == 'pt':
        titlepage='EDTL.EP - Detalha Departamento'
    else:
        titlepage='EDTL.EP - Department Detail'
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments, 'titlepage':titlepage, 'products': products, 'lang':lang, 'lang_data': lang_data,
    }
    template = 'inner_page/department/department.html'
    return render(request, template, context)

def department_detail(request,lang, hashid):
    objects = get_object_or_404(Department, hashed=hashid)
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    division = Division.objects.filter(department=objects)
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
        titlepage='EDTL.EP - Detalla Departamentu'
    elif lang == 'pt':
        titlepage='EDTL.EP - Detalha Departamento'
    else:
        titlepage='EDTL.EP - Department Detail'
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products,  'lang':lang, 'lang_data': lang_data,\
            'objects': objects, 'titlepage':titlepage, 'divisions':division
    }
    template = 'inner_page/department/department.html'
    return render(request, template, context)

def division_detail(request,lang, hashid, hashid2):
    objects = get_object_or_404(Division, hashed=hashid)
    department = get_object_or_404(Department, hashed=hashid2)
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
        titlepage='EDTL.EP - Detalla Divisaun'
    elif lang == 'pt':
        titlepage='EDTL.EP - Detalha Divisao'
    else:
        titlepage='EDTL.EP - Division Detail'
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,'objects': objects, \
                'department':department, 'titlepage':titlepage
    }
    template = 'inner_page/department/division.html'
    return render(request, template, context)

def video_list(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    gallery_categories = GalleryCategory.objects.all()
    today = datetime.now().date()
    ip = get_client_ip(request)
    if IpModel.objects.filter(ip=ip).exists():
        if IpModel.objects.filter(ip=ip, datetime__contains=today):
            pass
        else:
            IpModel.objects.create(ip=ip)
    else:
        IpModel.objects.create(ip=ip)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products, 'gallery_categories':gallery_categories, 'lang':lang, 'lang_data': lang_data,
    }
    template = 'inner_page/gallery/video_list.html'
    return render(request, template, context)


def faq_list(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    objects = Faq.objects.filter(is_active=True)
    paginator = Paginator(objects, 5)
    page_number = request.GET.get('page')
    today = datetime.now().date()
    ip = get_client_ip(request)
    if IpModel.objects.filter(ip=ip).exists():
        if IpModel.objects.filter(ip=ip, datetime__contains=today):
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
    template = 'inner_page/faq/faq_list.html'
    return render(request, template, context)

def faq_detail(request,lang,hashid):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    objects = get_object_or_404(Faq, hashed=hashid)
    today = datetime.now().date()
    ip = get_client_ip(request)
    if IpModel.objects.filter(ip=ip).exists():
        if IpModel.objects.filter(ip=ip, datetime__contains=today):
            pass
        else:
            IpModel.objects.create(ip=ip)
    else:
        IpModel.objects.create(ip=ip)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP', \
            'departments':departments,'products': products,'lang':lang, 'lang_data': lang_data, 'objects':objects
    }
    template = 'inner_page/faq/faq_detail.html'
    return render(request, template, context)

def usm_login(request,lang):
    lang_data = lang_master(lang)
    group = request.user.groups.all()[0].name
    departments = Department.objects.all()
    subscribechoices = SubscribeChoice.objects.all()
    products = Product.objects.filter(is_active=True)

    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)

    return redirect('redirect-home')


# 
def varanda2(request):
    form = NewsUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsUser.objects.filter(email=instance.email).exists():
            messages.warning(
                request, 'Your Email Already exists in our database', 'alert alert-warning alert-dismissible fade show')
        else:
            instance.save()
            messages.success(request, 'Your email has been submitted to the database',
                             'alert alert-success alert-dismissible fade show')
            subject = "Thank You For Joining Our Newsletter"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            with open(settings.BASE_DIR + "news/templates/email/signup_email.txt") as f:
                signup_message = f.read()
            message = EmailMultiAlternatives(
                subject=subject, body=signup_message, from_email=from_email, to=to_email)
            html_template = get_template(
                "email/signup_email.html").render()
            message.attach_alternative(html_template, "text/html")
            message.send()
            form = NewsUserSignUpForm()
            context = {
                'form': form
            }
            template = 'main/layout.html'
            return redirect('varanda')
    context = {
        'form': form
    }
    template = 'main/layout.html'
    return render(request, template, context)

def showFirebaseJS(request):
    data='importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-app.js");' \
         'importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-messaging.js"); ' \
         'var firebaseConfig = {' \
         '        apiKey: "AIzaSyAyrR2dgbPE11g6RJCXZ8-SR0tTBlbYToI",' \
         '        authDomain: "edtl-website.firebaseapp.com",' \
         '        databaseURL: "",' \
         '        projectId: "edtl-website",' \
         '        storageBucket: "edtl-website.appspot.com",' \
         '        messagingSenderId: "1029992166043",' \
         '        appId: "1:1029992166043:web:c48c04f8246ac1bbeacc3e",' \
         '        measurementId: "G-FJY07M0N2N"' \
         ' };' \
         'firebase.initializeApp(firebaseConfig);' \
         'const messaging=firebase.messaging();' \
         'messaging.setBackgroundMessageHandler(function (payload) {' \
         '    console.log(payload);' \
         '    const notification=JSON.parse(payload);' \
         '    const notificationOption={' \
         '        body:notification.body,' \
         '        icon:notification.icon' \
         '    };' \
         '    return self.registration.showNotification(payload.notification.title,notificationOption);' \
         '});'

    return HttpResponse(data,content_type="text/javascript")

def search(request,lang):
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
        titlepage='Buks'
    elif lang == 'pt':
        titlepage='Procurar'
    else:
        titlepage='Search'
    query = request.GET.get("s")    
    event_list = None
    announcement_list = None
    vacancy_list = None
    tender_list = None
    if query:
        if len(query) >= 3:
            if lang == 'tt':
                event_list =  Event.objects.filter(is_active=True, name_tet__icontains=query).distinct()
                announcement_list = Announcement.objects.filter(is_active=True, title_tet__icontains=query).distinct()
                vacancy_list = Vacancy.objects.filter(is_active=True, title_tet__icontains=query).distinct()
                tender_list = Tender.objects.filter(is_active=True, title_tet__icontains=query).distinct()
            elif lang == 'pt':
                event_list =  Event.objects.filter(is_active=True, name_por__icontains=query).distinct()
                announcement_list = Announcement.objects.filter(is_active=True, title_por__icontains=query).distinct()
                vacancy_list = Vacancy.objects.filter(is_active=True, title_por__icontains=query).distinct()
                tender_list = Tender.objects.filter(is_active=True, title_por__icontains=query).distinct()
            elif lang == 'en':
                event_list =  Event.objects.filter(is_active=True, name_eng__icontains=query).distinct()
                announcement_list = Announcement.objects.filter(is_active=True, title_eng__icontains=query).distinct()
                vacancy_list = Vacancy.objects.filter(is_active=True,title_eng__icontains=query).distinct()
                tender_list = Tender.objects.filter(is_active=True, title_eng__icontains=query).distinct()
        else:
            messages.error(request,'Please type more than 3 characters')
            return redirect('search-list', lang)
    else:
        pass
    print(vacancy_list)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products,'lang':lang, 'lang_data': lang_data, 'titlepage':titlepage,\
            'event_list':event_list, 'announcement_list':announcement_list, 'vacancy_list':vacancy_list, 'tender_list':tender_list
    }
    template = 'inner_page/search_list.html'
    return render(request, template, context)