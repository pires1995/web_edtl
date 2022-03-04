from django.urls import path
from . import views

urlpatterns = [
	path('approver/badge/', views.view_notif_appr_badge),
	path('approver/body/', views.view_notif_appr_body),
	path('approver/app/badge/', views.view_notif_appoint_badge),
	path('approver/app/body/', views.view_notif_appoint_body),
	path('approver/finance/badge/', views.view_notif_finance_badge),
	path('approver/finance/body/', views.view_notif_finance_body),
]