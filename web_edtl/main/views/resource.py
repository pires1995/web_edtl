
from django.shortcuts import render, redirect, get_object_or_404
from main.utils_lang import lang_master
from departments.models import Department
from product.models import Product

def resource_detail(request,lang, hashid):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    objects = get_object_or_404(Product, hashed=hashid)
    if lang == 'tt':
        titlepage='EDTL.EP - Produtu'
    elif lang == 'pt':
        titlepage='EDTL.EP - Produto'
    else:
        titlepage='EDTL.EP - Product'
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP',\
            'departments':departments, 'titlepage':titlepage, 'objects':objects, 'products': products,'lang':lang, 'lang_data': lang_data,
    }
    template = 'inner_page/resource.html'
    return render(request, template, context)