from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from news.models import News, NewsCategory
from datetime import datetime
from django.db.models import Count, Q
from appointment.models import Appointment
from news.models import NewsUser
from finance.models import Client
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
def dashboard(request):
    group = request.user.groups.all()[0].name
    client = Client.objects.filter(is_active=True).count()
    appointment = Appointment.objects.filter(is_done=True).count()
    subusers = NewsUser.objects.all().count()
    context ={
        'group': group, 'title': 'Dashboard', \
            'client': client, 'appointment': appointment, 'subusers': subusers
    }
    return render(request, 'web_admin/home.html', context)
