from django.urls import path
from . import views
urlpatterns = [
    # NEWS USER
    path('about-list/', views.about_list, name='admin-about-list'),
    path('about-add/', views.about_add, name='admin-about-add'),
    path('about-update/<str:hashid>/', views.about_update, name='admin-about-update'),
    path('service-list/', views.service_list, name='admin-service-list'),
    path('service-add/', views.service_add, name='admin-service-add'),
    path('service-update/<str:hashid>/', views.service_update, name='admin-service-update'),
    path('service-detail/<str:hashid>/', views.service_detail, name='admin-service-detail'),
    path('service-activate/<str:hashid>/', views.service_activate, name='admin-service-activate'),
    path('service-deactivate/<str:hashid>/', views.service_deactivate, name='admin-service-deactivate'),
    path('view-pdf/<str:hashid>/', views.view_pdf, name='admin-view-pdf'),



    # TEAM
    path('team-list/', views.list_team, name='admin-team-list'),
    # DIVISON
    path('division-profile-add/', views.add_division_profile, name='admin-division-profile-add'),
    path('division-profile-update/<str:hashid>/', views.update_division_profile, name='admin-division-profile-update'),
    # EMPLOYEE
    path('employee-add/', views.add_employee, name='admin-employee-add'),
    path('employee-update/<str:hashid>/', views.update_employee, name='admin-employee-update'),
    # POSITION
    path('position-add/', views.add_team, name='admin-position-add'),
    path('position-update/<str:hashid>/', views.update_team, name='admin-position-update'),

    path('administrator/deliverasaun-list/', views.deliverasaun_list, name='admin-deliverasaun-list'),
    path('administrator/deliverasaun-add/', views.deliverasaun_add, name='admin-deliverasaun-add'),
    path('administrator/deliverasaun-update/<str:hashid>/', views.deliverasaun_update, name='admin-deliverasaun-update'),
    path('administrator/deliverasaun-detail/<str:hashid>/', views.deliverasaun_detail, name='admin-deliverasaun-detail'),
    path('administrator/deliverasaun-activate/<str:hashid>/', views.deliverasaun_activate, name='admin-deliverasaun-activate'),
    path('administrator/deliverasaun-deactivate/<str:hashid>/', views.deliverasaun_deactivate, name='admin-deliverasaun-deactivate'),
]