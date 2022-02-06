from django.urls import path
from . import views

urlpatterns = [
    # CLIENT
    path('client-list/', views.client_list, name='admin-client-list'),
    path('client-add/', views.client_add, name='admin-client-add'),
    path('client-detail/<str:hashid>/', views.client_detail, name='admin-client-detail'),
    # BILL
    path('bill-list/', views.bill_list, name='admin-bill-list'),
    path('bill-detail/<str:hashid>/', views.bill_detail, name='admin-bill-detail'),
    path('bill-approve/<str:hashid>/', views.bill_approve, name='admin-bill-approve'),
]
