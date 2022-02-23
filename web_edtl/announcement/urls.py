from django.urls import path
from . import views
urlpatterns = [
    

    path('', views.announcement_list, name='admin-announcement-list'),
    path('admin/announcement-add/', views.announcement_add, name='admin-announcement-add'),
    path('admin/announcement-detail/<str:hashid>', views.announcement_detail, name='admin-announcement-detail'),
    path('admin/announcement-update/<str:hashid>/',
            views.announcement_update, name='admin-announcement-update'),
    path('admin/announcement-activate/<str:hashid>/',
            views.announcement_activate, name="admin-announcement-activate"),
    path('admin/announcement-deactivate/<str:hashid>/',
            views.announcement_deactivate, name="admin-announcement-deactivate"),
        #ANNOUNCEMENT SEND NOTIF
    path('send-announcement/<str:hashid>/', views.announcement_send_notif,
         name='admin-announcement-send')
]