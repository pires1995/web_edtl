from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm
urlpatterns = [
    path('', views.varanda, name="varanda"),

    # USERS
    path('users/', views.user_lists, name='admin-user-lists'),
    path('users/add', views.user_add, name='admin-user-add'),
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
