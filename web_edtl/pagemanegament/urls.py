from django.urls import path
from . import views

urlpatterns = [
    path('administrator/pagemanegament-list/', views.pagemanegament_list, name='admin-pagemanegament-list'),
    path('administrator/pagemanegament-add/', views.pagemanegament_add, name='admin-pagemanegament-add'),
    path('administrator/pagemanegament-update/<str:hashid>/', views.pagemanegament_update, name='admin-pagemanegament-update'),
    path('administrator/pagemanegament-detail/<str:hashid>/', views.pagemanegament_detail, name='admin-pagemanegament-detail'),
    path('administrator/pagemanegament-activate/<str:hashid>/', views.pagemanegament_activate, name='admin-pagemanegament-activate'),
    path('administrator/pagemanegament-deactivate/<str:hashid>/', views.pagemanegament_deactivate, name='admin-pagemanegament-deactivate'),

]
