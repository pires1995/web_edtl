from django.shortcuts import render, redirect
from news.forms import NewsUserSignUpForm
from news.models import NewsUser
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template
from main.utils_lang import lang_master
from departments.models import Department
from product.models import Product
def vacancy_list(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'EDTL, EP', 'lang':lang, 'lang_data': lang_data, \
            'departments':departments,'products': products,
    }
    template = 'inner_page/recruitment/vacancy_list.html'
    return render(request, template, context)


def internships_list(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en',\
            'departments':departments,'products': products,'title': 'EDTL, EP', 'lang':lang, 'lang_data': lang_data,
    }
    template = 'inner_page/recruitment/internships_list.html'
    return render(request, template, context)