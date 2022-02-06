from django.urls import path
from . import views

urlpatterns = [
    # ALBUM
    path('album-list/', views.album_list, name='admin-album-list'),
    path('album-add/', views.album_add, name='admin-album-add'),
    path('album-update/<str:hashid>/', views.album_update, name='admin-album-update'),
    path('album-detail/<str:hashid>/', views.album_detail, name='admin-album-detail'),
    # GALLERY
    path('gallery-add/<str:hashid>/', views.gallery_add, name='admin-gallery-add'),
    path('gallery-update/<str:hashid>/', views.gallery_update, name='admin-gallery-update'),

]