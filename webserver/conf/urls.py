"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path, include
from django.conf import settings

urlpatterns = [
    path('react/', include('react.urls', namespace='react')),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('home/', include('home.urls', namespace='home')),
    path('', include('home.urls', namespace='index')),
    path('ksh7194/', admin.site.urls),
    path('bookmark/', include('bookmark.urls', namespace='bookmark')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('pubmed_api/', include('pubmed_api.urls', namespace='pubmed_api')),
    path('form/', include('form.urls', namespace='form')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(
            re_path(r'^__debug__/', include(debug_toolbar.urls)),)
