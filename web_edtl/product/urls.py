from django.urls import path
from . import views

urlpatterns = [
    path('product-list/', views.product_list, name='admin-product-list'),
    path('product-add/', views.product_add, name='admin-product-add'),
    path('product-update/<str:hashid>/', views.product_update, name='admin-product-update'),
    path('product-detail/<str:hashid>/', views.product_detail, name='admin-product-detail'),

]