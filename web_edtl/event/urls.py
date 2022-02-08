from django.urls import path
from . import views

urlpatterns = [
    path('event-list/', views.event_list, name='admin-event-list'),
    path('event-add/', views.event_add, name='admin-event-add'),
    path('event-update/<str:hashid>/', views.event_update, name='admin-event-update'),
    path('event-detail/<str:hashid>/', views.event_detail, name='admin-event-detail'),
    path('event-activate/<str:hashid>/', views.event_activate, name='admin-event-activate'),
    path('event-deactivate/<str:hashid>/', views.event_deactivate, name='admin-event-deactivate'),

]
