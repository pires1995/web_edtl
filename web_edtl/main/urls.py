from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm
from django.views.generic.base import RedirectView

urlpatterns = [
    path('home/<str:lang>/', views.home, name="home"),
    path('inicio/<str:lang>/', views.inicio, name="inicio"),
    path('varanda/<str:lang>/', views.varanda, name="varanda"),
    path('', RedirectView.as_view(url='home/en/'), name="redirect-home"),
    
#     NEWS
    path('main-news/<str:lang>/', views.news_list, name="news-list"),
    path('main-news-detail/<str:lang>/', views.news_detail, name="news-detail"),
    
#     ABOUT
    path('who-we-are/<str:lang>/', views.who_we_are, name="who-we-are"),
    path('what-we-do/<str:lang>/', views.what_we_do, name="what-we-do"),
    path('board-profile/<str:lang>/', views.board_profile, name="board-profile"),

#     RESOURCE
    path('resource/<str:lang>/<str:hashid>/', views.resource_detail, name="resource-detail"),

    # DEPARTMENT
    path('department/<str:lang>/', views.department, name="department-list"),
    path('department/<str:lang>/<str:hashid>/', views.department_detail, name="department-detail"),
    path('division/<str:lang>/', views.division_detail, name="division-detail"),

    # EVENTS
    path('event-list/<str:lang>/', views.event_list, name="event-list"),
    path('event-detail/<str:lang>/', views.event_detail, name="event-detail"),

    # REPORT
    path('report-list/<str:lang>/', views.report_list, name="report-list"),
    path('report-detail/<str:lang>/', views.report_detail, name="report-detail"),

    # DOCUMENTARY
    path('documentary-list/<str:lang>/', views.documentary_list, name="documentary-list"),
    path('documentary-detail/<str:lang>/', views.documentary_detail, name="documentary-detail"),

    # RECRUITMENTS
    path('vacancy-list/<str:lang>/', views.vacancy_list, name="vacancy-list"),
    path('internships-list/<str:lang>/', views.internships_list, name="internships-list"),

    # PROCURAMENTS
    path('tender-list/<str:lang>/', views.tender_list, name="tender-list"),
    path('guideline-list/<str:lang>/', views.guideline_list, name="guideline-list"),

    # PROJECT
    path('project-new-list/<str:lang>/', views.project_new_list, name="new-list"),
    path('project-ongoing-list/<str:lang>/', views.project_ongoing_list, name="ongoing-list"),
    path('project-ongoing-detail/<str:lang>/', views.project_ongoing_detail, name="ongoing-detail"),
    path('project-new-detail/<str:lang>/', views.project_new_detail, name="new-detail"),

    # ALBUM
    path('album-list/<str:lang>/', views.album_list, name="album-list"),
    path('album-detail/<str:lang>/', views.album_detail, name="album-detail"),

    # VIDEO
    path('video-list/<str:lang>/', views.video_list, name="video-list"),

    # APPOINTMENT
    path('appointment/<str:lang>/', views.appointment, name="appointment"),

    # FAQ
    path('faq-detail/<str:lang>/', views.faq_detail, name="faq-detail"),

    
    
    
    
    
    
    
    # USERS
    path('users/', views.user_lists, name='admin-user-lists'),
    path('users/add/', views.user_add, name='admin-user-add'),
    path('users/update/<str:hashid>/',
         views.user_update, name='admin-user-update'),
    path('users/activate/<str:hashid>/',
         views.user_activate, name='admin-user-activate'),
    path('users/deactivate/<str:hashid>/',
         views.user_deactivate, name='admin-user-deactivate'),

    # ADMINISTRATOR
    path('administrator/', views.dashboard, name="admin-dashboard"),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='web_admin/login.html',
         authentication_form=UserLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='web_admin/logout.html'), name='logout'),
]
