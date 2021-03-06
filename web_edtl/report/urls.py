from django.urls import path
from . import views

urlpatterns = [
    path('report-list/', views.report_list, name='admin-report-list'),
    path('report-add/', views.report_add, name='admin-report-add'),
    path('report-update/<str:hashid>/', views.report_update, name='admin-report-update'),
    path('report-detail/<str:hashid>/', views.report_detail, name='admin-report-detail'),
    path('report-activate/<str:hashid>/', views.report_activate, name='admin-report-activate'),
    path('report-deactivate/<str:hashid>/', views.report_deactivate, name='admin-report-deactivate'),
]