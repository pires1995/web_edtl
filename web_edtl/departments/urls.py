from django.urls import path
from . import views
urlpatterns = [
    # DEPARTMENT
    path('department-list/', views.department_list, name='admin-department-list'),
    path('department-add/', views.department_add, name='admin-department-add'),
    path('department-update/<str:hashid>/', views.department_update, name='admin-department-update'),
    path('department-detail/<str:hashid>/', views.department_detail, name='admin-department-detail'),

    # DIVISION
    path('division-list/', views.division_list, name='admin-division-list'),
    path('division-add/', views.division_add, name='admin-division-add'),
    path('division-update/<str:hashid>/', views.division_update, name='admin-division-update'),
    path('division-detail/<str:hashid>/', views.division_detail, name='admin-division-detail'),

]