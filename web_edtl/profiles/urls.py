from django.urls import path
from . import views
urlpatterns = [
    # NEWS USER
    path('about-list/', views.about_list, name='admin-about-list'),
    path('about-add/', views.about_add, name='admin-about-add'),
    path('about-update/<str:hashid>/', views.about_update, name='admin-about-update'),
    path('view-pdf/<str:hashid>/', views.view_pdf, name='admin-view-pdf'),


    # TEAM
    path('team-list/', views.list_team, name='admin-team-list'),
    # DIVISON
    path('division-add/', views.add_division, name='admin-division-add'),
    path('division-update/<str:hashid>/', views.update_division, name='admin-division-update'),
    # EMPLOYEE
    path('employee-add/', views.add_employee, name='admin-employee-add'),
    path('employee-update/<str:hashid>/', views.update_employee, name='admin-employee-update'),
    # POSITION
    path('position-add/', views.add_team, name='admin-position-add'),
    path('position-update/<str:hashid>/', views.update_team, name='admin-position-update'),
]