from django.shortcuts import render, redirect
from news.forms import NewsUserSignUpForm
from news.models import NewsUser
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template
from main.utils_lang import lang_master
from profiles.models import Position
from departments.models import Department
from product.models import Product
def who_we_are(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en',\
            'departments':departments,'products': products,'title': 'EDTL, EP', 'lang':lang, 'lang_data': lang_data,
    }
    template = 'inner_page/about/who_we_are.html'
    return render(request, template, context)

def what_we_do(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en',\
            'departments':departments,'products': products,'title': 'EDTL, EP', 'lang':lang, 'lang_data': lang_data,
    }
    template = 'inner_page/about/what_we_do.html'
    return render(request, template, context)

def board_profile(request,lang):
    lang_data = lang_master(lang)
    objects = Position.objects.all()
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en',\
            'departments':departments,'products': products,'title': 'EDTL, EP', 'lang':lang, 'lang_data': lang_data,
        'objects': objects
    }
    template = 'inner_page/about/board_profile.html'
    return render(request, template, context)