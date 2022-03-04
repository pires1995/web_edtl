from django.shortcuts import render, redirect
from django.contrib import messages
from main.utils_lang import lang_master
from departments.models import Department
from product.models import Product
from main.forms import AppointmentForm, SuggestionForm
from appointment.models import Appointment, Suggestion
from main.utils import getnewid
from appointment.models import ContactMunicipality
from custom.models import IpModel
from main.utils import get_client_ip
from datetime import datetime
from news.tasks import appoint_submit
from main.models import User
import re
def appointment(request,lang):
    today = datetime.now().date()
    ip = get_client_ip(request)
    if IpModel.objects.filter(ip=ip).exists():
        if IpModel.objects.filter(ip=ip, datetime__date=today):
            pass
        else:
            IpModel.objects.create(ip=ip)
    else:
        IpModel.objects.create(ip=ip)
    form = AppointmentForm()
    form2 = SuggestionForm()
    if 'appointment_form' in request.POST:
        newid, new_hashed = getnewid(Appointment)
        form = AppointmentForm(request.POST)
        fullname = request.POST.get('first_name')
        secretary = User.objects.filter(groups__name='secretary', is_active=True)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id = newid
            instance.hashed = new_hashed
            instance.save()
            for email_to in secretary:
                set_name = email_to.email
                set_name2 = re.split(r'[@.]', set_name)
                appoint_submit.delay(email_to.email,set_name2[0],fullname)
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
    contactMunicipality = ContactMunicipality.objects.filter(is_active=True).order_by('-municipality')
    titlepage = ''

    if lang == 'tt':
        titlepage='EDTL.EP - Kontaktu'
    elif lang == 'pt':
        titlepage='EDTL.EP - Contacto'
    else:
        titlepage='EDTL.EP - Contact'
    context = {
        'l1': 'tt', 'l2': 'pt', 'l3': 'en','title': 'Appointment', \
            'departments':departments,'form':form,'form2':form2, 'products': products, 'lang':lang, 'lang_data': lang_data,\
                'contactMunicipality':contactMunicipality, 'titlepage':titlepage
    }
    template = 'inner_page/appointment.html'
    return render(request, template, context)