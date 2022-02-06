from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from news.models import News
# Create your views here.


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