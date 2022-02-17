from django.shortcuts import render, redirect, get_object_or_404
from news.forms import NewsUserSignUpForm
from news.models import NewsUser
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template
from main.utils_lang import lang_master
from news.models import News, NewsCategory, NewsImage
from departments.models import Department, Division
from product.models import Product
from gallery.models import GalleryCategory, Gallery, Album, Banner
from announcement.models import Announcement
from news.models import News
from faq.models import Faq
from procurament.models import Tender
from datetime import datetime
from django.core.paginator import Paginator
from django.conf import settings

def home(request, lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    banners = Banner.objects.filter(is_active=True)
    news_main = News.objects.filter(is_active=True, is_approved=True, language="English").last()
    news_recent = News.objects.filter(is_active=True, is_approved=True, language="English").order_by('-approved_date')[1:4]
    faq_home = Faq.objects.filter(is_active=True, is_homepage=True)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP','lang': lang, 'lang_data': lang_data,\
            'page': 'varanda', 'departments': departments, 'products': products, 'banners':banners, 
            'news_main': news_main, 'news_recent':news_recent, 'faq_home':faq_home
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
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP','lang': lang, 'lang_data': lang_data,\
            'page': 'varanda', 'departments': departments, 'products': products, 'banners':banners, 
            'news_main': news_main, 'news_recent':news_recent, 'faq_home':faq_home
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
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP','lang': lang, 'lang_data': lang_data,\
            'page': 'varanda', 'departments': departments, 'products': products, 'banners':banners, 
            'news_main': news_main, 'news_recent':news_recent, 'faq_home':faq_home
    }
    template = 'main/home.html'
    return render(request, template, context)
    
def department(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,
    }
    template = 'inner_page/department/department.html'
    return render(request, template, context)

def department_detail(request,lang, hashid):
    objects = get_object_or_404(Department, hashed=hashid)
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    division = Division.objects.filter(department=objects)
    products = Product.objects.filter(is_active=True)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products,  'lang':lang, 'lang_data': lang_data,\
            'objects': objects, 'divisions':division
    }
    template = 'inner_page/department/department.html'
    return render(request, template, context)

def division_detail(request,lang, hashid, hashid2):
    objects = get_object_or_404(Division, hashed=hashid)
    department = get_object_or_404(Department, hashed=hashid2)
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,'objects': objects, \
                'department':department
    }
    template = 'inner_page/department/division.html'
    return render(request, template, context)

def video_list(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    gallery_categories = GalleryCategory.objects.all()
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
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP', \
            'departments':departments,'products': products,'lang':lang, 'lang_data': lang_data, 'objects':objects
    }
    template = 'inner_page/faq/faq_detail.html'
    return render(request, template, context)

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
