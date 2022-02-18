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
from main.forms import AppointmentForm, SuggestionForm
from appointment.models import Appointment, Suggestion
from main.utils import getnewid

def appointment(request,lang):
    form = AppointmentForm()
    form2 = SuggestionForm()
    if 'appointment_form' in request.POST:
        newid, new_hashed = getnewid(Appointment)
        form = AppointmentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id = newid
            instance.hashed = new_hashed
            instance.save()
            messages.success(request, f'Successfully Submit Appointment')
            return redirect('appointment', lang)
    elif 'suggestion_form' in request.POST:
        newid, new_hashed = getnewid(Suggestion)
        form2 = SuggestionForm(request.POST)
        if form2.is_valid():
            instance2 = form2.save(commit=False)
            instance2.id = newid
            instance2.hashed = new_hashed
            instance2.save()
            messages.success(request, f'Successfully Submit Suggestion')
            return redirect('appointment', lang)
    lang_data = lang_master(lang)
    departments = Department.objects.all()
    products = Product.objects.filter(is_active=True)
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'Appointment', \
            'departments':departments,'form':form,'form2':form2, 'products': products, 'lang':lang, 'lang_data': lang_data,
    }
    template = 'inner_page/appointment.html'
    return render(request, template, context)