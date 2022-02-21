from django.urls import path
from . import views
urlpatterns = [
    # NEWS USER
    path('unsubscribe/', views.news_unsubscribed, name='news-user-unsubscribe'),

    # NEWS STAFF
    path('', views.news_list, name='admin-news-list'),
    path('news-add/', views.news_add, name='admin-news-add'),
    path('news-detail/<str:hashid>', views.news_detail, name='admin-news-detail'),
    path('news-update/<str:hashid>/',
         views.news_update, name='admin-news-update'),
    path('news-image-add/<str:hashid>/',
         views.news_image_add, name='admin-news-image-add'),
    path('news-image-update/<str:hashid>/<str:hashid2>/',
         views.news_image_update, name='admin-news-image-update'),
    path('news-image-delete/<str:hashid>/<str:hashid2>/',
         views.news_image_delete, name='admin-news-image-delete'),
    path('news-activate/<str:hashid>/',
         views.news_activate, name="admin-news-activate"),
    path('news-deactivate/<str:hashid>/',
         views.news_deactivate, name="admin-news-deactivate"),
    path('news-sent/<str:hashid>/',
         views.news_sent, name="admin-news-sent"),
    path('news-comments-list',
         views.news_comments_list, name="admin-news-comment-list"),
    path('news-comments-detail/<str:hashid>/',
         views.news_comments_detail, name="admin-news-comment-detail"),
    path('news-comments-approved/<str:hashid>/',
         views.news_comments_approved, name="admin-news-comment-approved"),
    path('news-comments-reject/<str:hashid>/',
         views.news_comments_reject, name="admin-news-comment-reject"),
    path('news-comments-delete/<str:hashid>/',
         views.news_comments_delete, name="admin-news-comment-delete"),

    # NEWS COORDINATOR
    path('admin-request-news/', views.news_approval_request_list,
         name='admin-news-request-list'),
    path('admin-approved-news/', views.news_approved_list,
         name='admin-news-approved-list'),
    path('admin-approve-news/<str:hashid>/', views.news_approved,
         name='admin-news-approve'),

     #TEST
    path('send-news/<str:hashid>/', views.news_send,
         name='admin-news-send')
]
