from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from news.models import News
from appointment.models import Appointment
from finance.models import Bill
# Create your views here.

@login_required
def view_notif_appr_badge(request):
    group = request.user.groups.all()[0].name
    dt_tot, dt_news = 0,0
    if group == 'coodinator':
        dt_news = News.objects.filter(is_sent=True, is_approved=False).all().count()
    dt_tot = dt_news
    return JsonResponse({'value': dt_tot})

@login_required
def view_notif_appr_body(request):
	group = request.user.groups.all()[0].name
	data1 = 0
	if group == "coodinator":
		data1 = News.objects.filter(is_sent=True, is_approved=False)\
				.all().count()
	
	return JsonResponse({'value1':data1})

@login_required
def view_notif_appoint_badge(request):
    group = request.user.groups.all()[0].name
    dt_tot, dt_app = 0,0
    if group == 'secretary':
        dt_app = Appointment.objects.filter(is_approved=False,is_reject=False).all().count()
    dt_tot = dt_app
    return JsonResponse({'value': dt_tot})

@login_required
def view_notif_appoint_body(request):
	group = request.user.groups.all()[0].name
	data1 = 0
	if group == "secretary":
		data1 = Appointment.objects.filter(is_approved=False,is_reject=False)\
				.all().count()
	
	return JsonResponse({'value1':data1})

@login_required
def view_notif_finance_badge(request):
    group = request.user.groups.all()[0].name
    dt_tot, dt_app = 0,0
    if group == 'finance':
        dt_app = Bill.objects.filter(is_done=False).all().count()
    dt_tot = dt_app
    return JsonResponse({'value': dt_tot})

@login_required
def view_notif_finance_body(request):
	group = request.user.groups.all()[0].name
	data1 = 0
	if group == "finance":
		data1 = Bill.objects.filter(is_done=False)\
				.all().count()
	
	return JsonResponse({'value1':data1})