from django.urls import path
from . import views

urlpatterns = [
    # VAGA
    path('vacancy-list/', views.vacancy_list, name='admin-vacancy-list'),
    path('vacancy-add/', views.vacancy_add, name='admin-vacancy-add'),
    path('vacancy-update/<str:hashid>/', views.vacancy_update, name='admin-vacancy-update'),
    path('vacancy-detail/<str:hashid>/', views.vacancy_detail, name='admin-vacancy-detail'),
    path('vacancy-activate/<str:hashid>/', views.vacancy_activate, name='admin-vacancy-activate'),
    path('vacancy-deactivate/<str:hashid>/', views.vacancy_deactivate, name='admin-vacancy-deactivate'),
    # INTERNSHIPS
    path('internships-list/', views.internships_list, name='admin-internships-list'),
    path('internships-add/', views.internships_add, name='admin-internships-add'),
    path('internships-update/<str:hashid>/', views.internships_update, name='admin-internships-update'),
    path('internships-detail/<str:hashid>/', views.internships_detail, name='admin-internships-detail'),
    path('internships-activate/<str:hashid>/', views.internships_activate, name='admin-internships-activate'),
    path('internships-deactivate/<str:hashid>/', views.internships_deactivate, name='admin-internships-deactivate'),
]