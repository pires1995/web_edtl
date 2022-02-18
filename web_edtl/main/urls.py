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
    path('news/<str:lang>/', views.news_list, name="news-list"),
    path('news-detail/<str:lang>/<str:year>/<str:month>/<str:hashid>/<str:titleseo>/', views.news_detail, name="news-detail"),
    
#     ABOUT
    path('who-we-are/<str:lang>/', views.who_we_are, name="who-we-are"),
    path('what-we-do/<str:lang>/', views.what_we_do, name="what-we-do"),
    path('board-profile/<str:lang>/', views.board_profile, name="board-profile"),
    path('board-detail/<str:hashid>/<str:lang>/', views.board_detail, name="board-detail"),

#     RESOURCE
    path('resource/<str:lang>/<str:hashid>/', views.resource_detail, name="resource-detail"),

    # DEPARTMENT
    path('department/<str:lang>/', views.department, name="department-list"),
    path('department/<str:lang>/<str:hashid>/', views.department_detail, name="department-detail"),
    path('division/<str:lang>/<str:hashid>/<str:hashid2>/', views.division_detail, name="division-detail"),

    # EVENTS
    path('event-list/<str:lang>/', views.event_list, name="event-list"),
    path('event-detail/<str:lang>/<str:hashid>/', views.event_detail, name="event-detail"),

    # REPORT
    path('report-list/<str:lang>/', views.report_list, name="report-list"),
    path('report-detail/<str:lang>/<str:hashid>/', views.report_detail, name="report-detail"),
    path('report-download/<str:hashid>/', views.report_download, name="report-download"),

    # DOCUMENTARY
    path('documentary-list/<str:lang>/', views.documentary_list, name="documentary-list"),
    path('documentary-list-filter/<str:lang>/<str:year>/', views.documentary_list_filter, name="documentary-list-filter"),
    path('documentary-detail/<str:lang>/<str:hashid>/', views.documentary_detail, name="documentary-detail"),

    # RECRUITMENTS
    path('vacancy-list/<str:lang>/', views.vacancy_list, name="vacancy-list"),
    path('internships-list/<str:lang>/', views.internships_list, name="internships-list"),
    path('volunteer-list/<str:lang>/', views.volunteer_list, name="volunteer-list"),
    path('vacancy-download/<str:hashid>/', views.vacancy_download, name="vacancy-download"),
    path('internships-download/<str:hashid>/', views.internships_download, name="internships-download"),
    path('volunteer-download/<str:hashid>/', views.volunteer_download, name="volunteer-download"),

    # PROCURAMENTS
    path('tender-list/<str:lang>/', views.tender_list, name="tender-list"),
    path('guideline-list/<str:lang>/', views.guideline_list, name="guideline-list"),
    path('policy-list/<str:lang>/', views.policy_list, name="policy-list"),
    path('tender-download/<str:hashid>/', views.tender_download, name="tender-download"),
    path('guideline-download/<str:hashid>/', views.guideline_download, name="guideline-download"),
    path('policy-download/<str:hashid>/', views.policy_download, name="policy-download"),

    # PROJECT
    path('project-new-list/<str:lang>/', views.project_new_list, name="new-list"),
    path('project-ongoing-list/<str:lang>/', views.project_ongoing_list, name="ongoing-list"),
    path('project-ongoing-detail/<str:lang>/<str:hashid>/', views.project_ongoing_detail, name="ongoing-detail"),
    path('project-new-detail/<str:lang>/<str:hashid>/', views.project_new_detail, name="new-detail"),

    # ALBUM
    path('album-list/<str:lang>/', views.album_list, name="album-list"),
    path('album-detail/<str:lang>/<str:hashid>/', views.album_detail, name="album-detail"),

    # VIDEO
    path('video-list/<str:lang>/', views.video_list, name="video-list"),

    # APPOINTMENT
    path('appointment/<str:lang>/', views.appointment, name="appointment"),

    # FAQ
    path('faq-list/<str:lang>/', views.faq_list, name="faq-list"),
    path('faq-detail/<str:lang>/<str:hashid>/', views.faq_detail, name="faq-detail"),
    # ANNOUNNCEMENT
    path('announcement-list/<str:lang>/', views.announcement_list, name="announcement-list"),
    path('announcement-detail/<str:lang>/<str:hashid>/', views.announcement_detail, name="announcement-detail"),


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

    # FMS
    path('fcm/login/', views.fms_login , name='fsm-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='web_admin/logout.html'), name='fsm-logout'),
    path('client-home/', views.client_home, name='client-home'),
    path('client-logout/', auth_views.LogoutView.as_view(template_name='fms/logout.html'), name='fsm-logout'),
    path('client-bill-list/', views.client_bill_list, name='bill-list'),
    path('client-bill-add/', views.client_bill_add, name='bill-add'),
    path('client-bill-detail/<str:hashid>', views.client_bill_detail, name='client-bill-detail'),


    # USM
    path('usm/login/<str:lang>/', views.usm_login , name='usm-login'),
]
