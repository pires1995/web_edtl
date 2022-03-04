from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from news.models import News, NewsCategory
from datetime import datetime
from django.db.models import Count, Q
from appointment.models import Appointment
from news.models import NewsUser
from finance.models import Client
from custom.decorators import allowed_users
from custom.models import FirebaseToken
from django.http import HttpResponse
from finance.models import Client, Bill
def month():
    month_name = {
        '1': 'January',
        '2': 'February',
        '3': 'March',
        '4': 'April',
        '5': 'May',
        '6': 'June',
        '7': 'July',
        '8': 'August',
        '9': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December',
    }

@login_required
@allowed_users(allowed_roles=['admin','media','coordinator', 'finance', 'secretary'])
def dashboard(request):
    group = request.user.groups.all()[0].name
    client = Client.objects.filter(is_active=True).count()
    appointment = Appointment.objects.filter(is_done=True).count()
    subusers = NewsUser.objects.all().count()
    appointment_approved = Appointment.objects.filter(is_approved=True).count()
    appointment_done = Appointment.objects.filter(is_done=True).count()
    appointment_incomming = Appointment.objects.filter(is_approved=False, is_reject=False).count()
    clients = Client.objects.all().count()
    bill_incoming = Bill.objects.filter(is_done=False).count()
    bill_done = Bill.objects.filter(is_done=True).count()
    context ={
        'group': group, 'title': 'Dashboard', \
        'appointment_approved':appointment_approved,\
        'appointment_done':appointment_done,'clients':clients,\
        'bill_incoming':bill_incoming, 'bill_done':bill_done,\
        'appointment_incomming':appointment_incomming,  'client': client, 'appointment': appointment, 'subusers': subusers
    }
    return render(request, 'web_admin/home.html', context)



def create_token(request, token):
    FirebaseToken.objects.create(token=token)
    return HttpResponse('')
        