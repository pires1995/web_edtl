from django.urls import path
from . import views

urlpatterns = [
    path('appointment-list/', views.appointment_list, name='admin-appointment-list'),
    path('appointment-approved-list/', views.appointment_approved_list, name='admin-appointment-approved-list'),
    path('appointment-reject-list/', views.appointment_reject_list, name='admin-appointment-reject-list'),
    path('appointment-detail/<str:hashid>/', views.appointment_detail, name='admin-appointment-detail'),
    path('appointment-done/<str:hashid>/', views.appointment_approved_done, name='admin-appointment-done'),
    path('appointment-not-done/<str:hashid>/', views.appointment_approved_not_done, name='admin-appointment-not-done'),
    path('contact-list/', views.contact_list, name='admin-contact-list'),
    path('contact-add/', views.contact_add, name='admin-contact-add'),
    path('contact-update/<str:hashid>/', views.contact_update, name='admin-contact-update'),
    path('contact-activate/<str:hashid>/', views.contact_activate, name='admin-contact-activate'),
    path('contact-deactivate/<str:hashid>/', views.contact_deactivate, name='admin-contact-deactivate'),
    path('contact-list/', views.contact_list, name='admin-contact-list'),
    path('suggestion-list/', views.suggestion_list, name='admin-suggestion-list'),
    path('suggestion-detail/<str:hashid>/', views.suggestion_detail, name='admin-suggestion-detail'),
]