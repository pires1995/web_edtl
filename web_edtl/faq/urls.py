from django.urls import path
from . import views

urlpatterns = [
    path('faq-list/', views.faq_list, name='admin-faq-list'),
    path('faq-add/', views.faq_add, name='admin-faq-add'),
    path('faq-update/<str:hashid>/', views.faq_update, name='admin-faq-update'),
    path('faq-detail/<str:hashid>/', views.faq_detail, name='admin-faq-detail'),

]
