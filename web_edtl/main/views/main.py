from django.shortcuts import render, redirect, get_object_or_404
from news.forms import NewsUserSignUpForm
from news.models import NewsUser
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template
from main.utils_lang import lang_master
from news.models import News, NewsCategory, NewsImage
from departments.models import Department
from product.models import Product
from gallery.models import GalleryCategory, Gallery, Album

def home(request, lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP','lang': lang, 'lang_data': lang_data,\
            'page': 'varanda', 'departments': departments, 'products': products
    }
    template = 'main/home.html'
    return render(request, template, context)


def inicio(request, lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    context = {
         'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP', 'lang': lang, 'lang_data': lang_data,\
             'page': 'varanda','products': products,'departments': departments
    }
    template = 'main/home.html'
    return render(request, template, context)

def varanda(request, lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    context = {
         'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP', 'lang':lang, 'lang_data': lang_data,\
             'page': 'varanda','products': products,'departments': departments
    }
    template = 'main/home.html'
    return render(request, template, context)

def news_list(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    if lang == 'l3':
        news_list = News.objects.filter(is_approved=True).order_by('-approved_date')
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,
    }
    template = 'inner_page/news_list.html'
    return render(request, template, context)


def news_detail(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP','products': products, 'departments':departments, 'lang':lang, 'lang_data': lang_data,
    }
    template = 'inner_page/news_detail.html'
    return render(request, template, context)

def resource_detail(request,lang, hashid):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    objects = get_object_or_404(Product, hashed=hashid)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments, 'objects':objects, 'products': products,'lang':lang, 'lang_data': lang_data,
    }
    template = 'inner_page/resource.html'
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
    products = Product.objects.filter(is_active=True)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products,  'lang':lang, 'lang_data': lang_data,\
            'objects': objects
    }
    template = 'inner_page/department/department.html'
    return render(request, template, context)

def division_detail(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,
    }
    template = 'inner_page/department/division.html'
    return render(request, template, context)


def event_list(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,
    }
    template = 'inner_page/event/list.html'
    return render(request, template, context)


def event_detail(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,
    }
    template = 'inner_page/event/detail.html'
    return render(request, template, context)

def report_list(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,
    }
    template = 'inner_page/report/list.html'
    return render(request, template, context)


def report_detail(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP', \
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,
    }
    template = 'inner_page/report/detail.html'
    return render(request, template, context)

def documentary_list(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    gallery_categories = GalleryCategory.objects.all()
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP', \
            'departments':departments,'products': products,'gallery_categories': gallery_categories, 'lang':lang, 'lang_data': lang_data,
    }
    template = 'inner_page/documentary.html'
    return render(request, template, context)

def documentary_detail(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,
    }
    template = 'inner_page/documentary_detail.html'
    return render(request, template, context)

def tender_list(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,
    }
    template = 'inner_page/procurament/tender.html'
    return render(request, template, context)

def guideline_list(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,
    }
    template = 'inner_page/procurament/guideline.html'
    return render(request, template, context)


def project_ongoing_list(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,
    }
    template = 'inner_page/project/ongoing.html'
    return render(request, template, context)

def project_ongoing_detail(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP', \
            'departments':departments, 'products': products, 'lang':lang, 'lang_data': lang_data,
    }
    template = 'inner_page/project/ongoing_detail.html'
    return render(request, template, context)

def project_new_list(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP', \
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,
    }
    template = 'inner_page/project/new.html'
    return render(request, template, context)

def project_new_detail(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP', \
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,
    }
    template = 'inner_page/project/new_detail.html'
    return render(request, template, context)

def album_list(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    gallery_categories = GalleryCategory.objects.all()
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,\
                'gallery_categories': gallery_categories
    }
    template = 'inner_page/gallery/album_list.html'
    return render(request, template, context)

def album_detail(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data,
    }
    template = 'inner_page/gallery/album_detail.html'
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

def faq_detail(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP', \
            'departments':departments,'products': products,'lang':lang, 'lang_data': lang_data,
    }
    template = 'inner_page/faq/faq_detail.html'
    return render(request, template, context)

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
