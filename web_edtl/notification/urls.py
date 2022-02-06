from django.urls import path
from . import views

urlpatterns = [
	path('approver/badge/', views.view_notif_appr_badge),
	path('approver/body/', views.view_notif_appr_body),
]