from django.shortcuts import render, redirect, get_object_or_404
from news.forms import NewsUserSignUpForm
from news.models import NewsUser
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template
from main.utils_lang import lang_master
from profiles.models import Position, About, Service
from departments.models import Department
from product.models import Product

def who_we_are(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    objects = About.objects.all().first()
    if lang == 'tt':
        legend = 'SE MAK AMI'
    elif lang == 'pt':
        legend = 'QUEM NÓS SOMOS'
    else:
        legend = 'WHO WE ARE'
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en', 'legend': legend, \
        'objects':objects, 'departments':departments,'products': products,'title': 'EDTL, EP', 'lang':lang, 'lang_data': lang_data,
    }
    template = 'inner_page/about/who_we_are.html'
    return render(request, template, context)

def what_we_do(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    objects = Service.objects.filter(is_active=True)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en',\
            'departments':departments,'products': products,'title': 'EDTL, EP', 'lang':lang, 'lang_data': lang_data, 'objects':objects
    }
    template = 'inner_page/about/what_we_do.html'
    return render(request, template, context)

def board_profile(request,lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    boardmembers = Position.objects.filter(group='Board Member')
    departments_board = Position.objects.filter(group='Department')
    divisions_board = Position.objects.filter(group='Division')
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en',\
            'departments':departments,'products': products,'title': 'EDTL, EP', 'lang':lang, 'lang_data': lang_data,
        'boardmembers': boardmembers, 'departments_board':departments_board,\
            'divisions_board':divisions_board
    }
    template = 'inner_page/about/board_profile.html'
    return render(request, template, context)

def board_detail(request, hashid, lang):
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    objects = get_object_or_404(Position, hashed=hashid)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en',\
            'departments':departments,'products': products,'title': 'EDTL, EP', 'lang':lang,
            'objects': objects, 'lang_data': lang_data,
    }
    template = 'inner_page/about/board_detail.html'
    return render(request, template, context)