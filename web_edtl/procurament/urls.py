from django.urls import path
from . import views

urlpatterns = [
    # TENDER
    path('tender-list/', views.tender_list, name='admin-tender-list'),
    path('tender-add/', views.tender_add, name='admin-tender-add'),
    path('tender-update/<str:hashid>/', views.tender_update, name='admin-tender-update'),
    path('tender-detail/<str:hashid>/', views.tender_detail, name='admin-tender-detail'),
    # GUIDELINES
    path('guidelines-list/', views.guidelines_list, name='admin-guidelines-list'),
    path('guidelines-add/', views.guidelines_add, name='admin-guidelines-add'),
    path('guidelines-update/<str:hashid>/', views.guidelines_update, name='admin-guidelines-update'),
    path('guidelines-detail/<str:hashid>/', views.guidelines_detail, name='admin-guidelines-detail'),
]