
from django.shortcuts import render, redirect, get_object_or_404
from main.utils_lang import lang_master
from departments.models import Department
from product.models import Product

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