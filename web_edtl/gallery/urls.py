from django.urls import path
from . import views

urlpatterns = [
    # ALBUM
    path('administrator/album-list/', views.album_list, name='admin-album-list'),
    path('administrator/album-add/', views.album_add, name='admin-album-add'),
    path('administrator/album-update/<str:hashid>/', views.album_update, name='admin-album-update'),
    path('administrator/album-detail/<str:hashid>/', views.album_detail, name='admin-album-detail'),
    path('administrator/album-activate/<str:hashid>/', views.album_activate, name='admin-album-activate'),
    path('administrator/album-deactivate/<str:hashid>/', views.album_deactivate, name='admin-album-deactivate'),
    # GALLERY
    path('administrator/gallery-add/<str:hashid>/', views.gallery_add, name='admin-gallery-add'),
    path('administrator/gallery-update/<str:hashid>/', views.gallery_update, name='admin-gallery-update'),
    # BANNER
    path('administrator/banner-list/', views.banner_list, name='admin-banner-list'),
    path('administrator/banner-add/', views.banner_add, name='admin-banner-add'),
    path('administrator/banner-update/<str:hashid>/', views.banner_update, name='admin-banner-update'),
    path('administrator/banner-detail/<str:hashid>/', views.banner_detail, name='admin-banner-detail'),
    path('administrator/banner-activate/<str:hashid>/', views.banner_activate, name='admin-banner-activate'),
    path('administrator/banner-deactivate/<str:hashid>/', views.banner_deactivate, name='admin-banner-deactivate'),
    # VIDEO
    path('administrator/video-list/', views.video_list, name='admin-video-list'),
    path('administrator/video-add/', views.video_add, name='admin-video-add'),
    path('administrator/video-update/<str:hashid>/', views.video_update, name='admin-video-update'),
    path('administrator/video-detail/<str:hashid>/', views.video_detail, name='admin-video-detail'),
    path('administrator/video-activate/<str:hashid>/', views.video_activate, name='admin-video-activate'),
    path('administrator/video-deactivate/<str:hashid>/', views.video_deactivate, name='admin-video-deactivate'),
]