from django.shortcuts import render, redirect, get_object_or_404
from main.utils_lang import lang_master
from departments.models import Department, Division
from product.models import Product
from report.models import Report
from django.core.paginator import Paginator
from django.http import FileResponse
from django.conf import settings

def report_list(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    lang_data = lang_master(lang)
    objects = Report.objects.filter(is_active=True)
    paginator = Paginator(objects, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data, 'page_obj': page_obj
    }
    template = 'inner_page/report/list.html'
    return render(request, template, context)


def report_detail(request,lang, hashid):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    objects = get_object_or_404(Report, hashed=hashid)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP', \
            'departments':departments,'products': products, 'lang':lang, 'lang_data': lang_data, 'objects': objects
    }
    template = 'inner_page/report/detail.html'
    return render(request, template, context)

def report_download(request, hashid):
	obj = get_object_or_404(Report, hashed=hashid)
	filename = str(settings.BASE_DIR)+str(obj.file.url)
	response = FileResponse(open(filename, 'rb'))
	return response