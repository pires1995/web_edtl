from django.urls import path
from . import views

urlpatterns = [
    # TENDER
    path('tender-list/', views.tender_list, name='admin-tender-list'),
    path('tender-add/', views.tender_add, name='admin-tender-add'),
    path('tender-update/<str:hashid>/', views.tender_update, name='admin-tender-update'),
    path('tender-detail/<str:hashid>/', views.tender_detail, name='admin-tender-detail'),
    path('tender-activate/<str:hashid>/', views.tender_activate, name='admin-tender-activate'),
    path('tender-deactivate/<str:hashid>/', views.tender_deactivate, name='admin-tender-deactivate'),
    # GUIDELINES
    path('guidelines-list/', views.guidelines_list, name='admin-guidelines-list'),
    path('guidelines-add/', views.guidelines_add, name='admin-guidelines-add'),
    path('guidelines-update/<str:hashid>/', views.guidelines_update, name='admin-guidelines-update'),
    path('guidelines-detail/<str:hashid>/', views.guidelines_detail, name='admin-guidelines-detail'),
    path('guidelines-activate/<str:hashid>/', views.guidelines_activate, name='admin-guidelines-activate'),
    path('guidelines-deactivate/<str:hashid>/', views.guidelines_deactivate, name='admin-guidelines-deactivate'),
    
    # POLICY
    path('policy-list/', views.policy_list, name='admin-policy-list'),
    path('policy-add/', views.policy_add, name='admin-policy-add'),
    path('policy-update/<str:hashid>/', views.policy_update, name='admin-policy-update'),
    path('policy-detail/<str:hashid>/', views.policy_detail, name='admin-policy-detail'),
    path('policy-activate/<str:hashid>/', views.policy_activate, name='admin-policy-activate'),
    path('policy-deactivate/<str:hashid>/', views.policy_deactivate, name='admin-policy-deactivate'),
]