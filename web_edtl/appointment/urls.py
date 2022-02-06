from django.urls import path
from . import views

urlpatterns = [
    path('appointment-list/', views.appointment_list, name='admin-appointment-list'),
    path('appointment-approved-list/', views.appointment_approved_list, name='admin-appointment-approved-list'),
    path('appointment-reject-list/', views.appointment_reject_list, name='admin-appointment-reject-list'),
    path('appointment-detail/<str:hashid>/', views.appointment_detail, name='admin-appointment-detail'),
    path('appointment-done/<str:hashid>/', views.appointment_approved_done, name='admin-appointment-done'),
    path('appointment-not-done/<str:hashid>/', views.appointment_approved_not_done, name='admin-appointment-not-done'),

]
