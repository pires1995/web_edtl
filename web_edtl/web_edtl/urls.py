
"""web_edtl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve
from main import views

urlpatterns = [
    path('', include('main.urls')),
    path('news-admin/', include('news.urls')),
    path('superuser/', admin.site.urls),
    path('profiles/', include('profiles.urls')),
    path('announcement/', include('announcement.urls')),
    path('departments/', include('departments.urls')),
    path('faq/', include('faq.urls')),
    path('recruitments/', include('recruitment.urls')),
    path('page-manegament/', include('pagemanegament.urls')),
    path('products/', include('product.urls')),
    path('reports/', include('report.urls')),
    path('appointments/', include('appointment.urls')),
    path('custom/', include('custom.urls')),
    path('fms/', include('finance.urls')),
    path('gallery/', include('gallery.urls')),
    path('projects/', include('project.urls')),
    path('procuraments/', include('procurament.urls')),
    path('events/', include('event.urls')),
    path('notifications/', include('notification.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('firebase-messaging-sw.js', views.showFirebaseJS, name='show-firebase'),

    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
