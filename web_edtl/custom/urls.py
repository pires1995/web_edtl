from django.urls import path
from . import views

urlpatterns = [
	path('ajax/load-posts/', views.load_posts, name='ajax_load_posts'),
	path('ajax/load-villages/', views.load_villages, name='ajax_load_villages'),
	path('profile/', views.ProfileUpdate, name="user-profile"),
	path('account/', views.AccountUpdate, name='user-account'),
	path('change/password/', views.UserPasswordChangeView.as_view(), name='user-change-password'),
	path('change/password/done/', views.UserPasswordChangeDoneView.as_view(), name='user-change-password-done'),
]