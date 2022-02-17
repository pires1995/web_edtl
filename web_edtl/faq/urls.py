from django.urls import path
from . import views

urlpatterns = [
    path('administrator/faq-list/', views.faq_list, name='admin-faq-list'),
    path('administrator/faq-add/', views.faq_add, name='admin-faq-add'),
    path('administrator/faq-update/<str:hashid>/', views.faq_update, name='admin-faq-update'),
    path('administrator/faq-detail/<str:hashid>/', views.faq_detail, name='admin-faq-detail'),
    path('administrator/faq-activate/<str:hashid>/', views.faq_activate, name='admin-faq-activate'),
    path('administrator/faq-deactivate/<str:hashid>/', views.faq_deactivate, name='admin-faq-deactivate'),
    path('administrator/faq-set-homepage/<str:hashid>/', views.faq_set_homepage, name='admin-faq-set-homepage'),
    path('administrator/faq-remove-homepage/<str:hashid>/', views.faq_remove_homepage, name='admin-faq-remove-homepage'),

]
