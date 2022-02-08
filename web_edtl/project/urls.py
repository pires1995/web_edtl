from django.urls import path
from . import views
urlpatterns = [
    # NEW PROJECT
    path('new-project-list/', views.new_project_list, name='admin-new-project-list'),
    path('new-project-add/', views.new_project_add, name='admin-new-project-add'),
    path('new-project-update/<str:hashid>/', views.new_project_update, name='admin-new-project-update'),
    path('new-project-detail/<str:hashid>/', views.new_project_detail, name='admin-new-project-detail'),
    # BUDGET
    path('new-project-add-budget/<str:hashid>/', views.new_project_add_budget, name='admin-new-project-add-budget'),
    path('new-project-update-budget/<str:hashid>/<str:hashid2>/', views.new_project_update_budget, name='admin-new-project-update-budget'),
    # LOCATION
    path('new-project-add-location/<str:hashid>/', views.new_project_add_location, name='admin-new-project-add-location'),
    path('new-project-update-location/<str:hashid>/<str:hashid2>/', views.new_project_update_location, name='admin-new-project-update-location'),

    # NEW PROJECT
    path('ongoing-project-list/', views.ongoing_project_list, name='admin-ongoing-project-list'),
    path('ongoing-project-add/', views.ongoing_project_add, name='admin-ongoing-project-add'),
    path('ongoing-project-update/<str:hashid>/', views.ongoing_project_update, name='admin-ongoing-project-update'),
    path('ongoing-project-detail/<str:hashid>/', views.ongoing_project_detail, name='admin-ongoing-project-detail'),
    # BUDGET
    path('ongoing-project-add-budget/<str:hashid>/', views.ongoing_project_add_budget, name='admin-ongoing-project-add-budget'),
    path('ongoing-project-update-budget/<str:hashid>/<str:hashid2>/', views.ongoing_project_update_budget, name='admin-ongoing-project-update-budget'),
    # LOCATION
    path('ongoing-project-add-location/<str:hashid>/', views.ongoing_project_add_location, name='admin-ongoing-project-add-location'),
    path('ongoing-project-update-location/<str:hashid>/<str:hashid2>/', views.ongoing_project_update_location, name='admin-ongoing-project-update-location'),

    path('new-project-activate/<str:hashid>/', views.new_project_activate, name='admin-new-project-activate'),
    path('new-project-deactivate/<str:hashid>/', views.new_project_deactivate, name='admin-new-project-deactivate'),
    path('ongoing-project-activate/<str:hashid>/', views.ongoing_project_activate, name='admin-ongoing-project-activate'),
    path('ongoing-project-deactivate/<str:hashid>/', views.ongoing_project_deactivate, name='admin-ongoing-project-deactivate'),
]