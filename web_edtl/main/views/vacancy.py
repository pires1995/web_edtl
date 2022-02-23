from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template
from main.utils_lang import lang_master
from departments.models import Department
from product.models import Product
from recruitment.models import Vacancy, Internships, Volunteer
from django.core.paginator import Paginator
from datetime import datetime
from django.http import FileResponse
from django.conf import settings
from pagemanegament.models import PageManegament

def vacancy_list(request,lang):
    today = datetime.now()
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    objects = Vacancy.objects.filter(is_active=True).order_by('-datetime')
    lang_data = lang_master(lang)
    paginator = Paginator(objects, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_description = ''
    if lang == 'tt':
        titlepage='EDTL.EP - Lista Vaga'
    elif lang == 'pt':
        titlepage='EDTL.EP - Lista Vaga'
    else:
        titlepage='EDTL.EP - Vacancy List'
    try:
        page_description = get_object_or_404(PageManegament, name='vacancy',is_active = True)
    except:
        page_description = ''
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP', 'lang':lang, 'lang_data': lang_data, \
            'departments':departments, 'page_description':page_description, 'titlepage':titlepage, 'products': products, 'page_obj':page_obj, 'today': today
    }
    template = 'inner_page/recruitment/vacancy_list.html'
    return render(request, template, context)

def vacancy_download(request, hashid):
	obj = get_object_or_404(Vacancy, hashed=hashid)
	filename = str(settings.BASE_DIR)+str(obj.file.url)
	response = FileResponse(open(filename, 'rb'))
	return response

def internships_list(request,lang):
    today = datetime.now()
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    objects = Internships.objects.filter(is_active=True).order_by('-datetime')
    lang_data = lang_master(lang)
    paginator = Paginator(objects, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_description = ''
    if lang == 'tt':
        titlepage='EDTL.EP - Lista Estagio'
    elif lang == 'pt':
        titlepage='EDTL.EP - Lista Estagio'
    else:
        titlepage='EDTL.EP - Internship List'
    try:
        page_description = get_object_or_404(PageManegament, name='internships',is_active = True)
    except:
        page_description = ''
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en',\
            'departments':departments,'products': products,'title': 'EDTL, EP', 'lang':lang, 'lang_data': lang_data,\
                'page_obj':page_obj, '':page_description, 'today': today, 'titlepage':titlepage
    }
    template = 'inner_page/recruitment/internships_list.html'
    return render(request, template, context)

def internships_download(request, hashid):
	obj = get_object_or_404(Internships, hashed=hashid)
	filename = str(settings.BASE_DIR)+str(obj.file.url)
	response = FileResponse(open(filename, 'rb'))
	return response

def volunteer_list(request,lang):
    today = datetime.now()
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    objects = Volunteer.objects.filter(is_active=True).order_by('-datetime')
    lang_data = lang_master(lang)
    paginator = Paginator(objects, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_description = ''
    if lang == 'tt':
        titlepage='EDTL.EP - Lista Voluntariu'
    elif lang == 'pt':
        titlepage='EDTL.EP - Lista Voluntario'
    else:
        titlepage='EDTL.EP - Volunteer List'
    try:
        page_description = get_object_or_404(PageManegament, name='internships',is_active = True)
    except:
        page_description = ''
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en',\
            'departments':departments,'products': products,'title': 'EDTL, EP', 'lang':lang, 'lang_data': lang_data,\
                'page_obj':page_obj,'page_description':page_description, 'today': today, 'titlepage':titlepage
    }
    template = 'inner_page/recruitment/volunteer.html'
    return render(request, template, context)

def volunteer_download(request, hashid):
	obj = get_object_or_404(Volunteer, hashed=hashid)
	filename = str(settings.BASE_DIR)+str(obj.file.url)
	response = FileResponse(open(filename, 'rb'))
	return response