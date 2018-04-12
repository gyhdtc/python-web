"""zwh2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from mysite import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.blog),
    url(r'^blog/', views.blog),
    url(r'^about/', views.about),
    url(r'^weixin/', views.weixin),
    url(r'^write', views.write),
    url(r'^save', views.save),
    url(r'^contact', views.contact),
    url(r'^simple', views.simple),
    url(r'^article/([0-9]+)', views.article),

    # url(r'^lostpassword/', views.lost),
    # url(r'^hello/',views.hello),
    # url(r'^logup/',views.logup),
    # url(r'^login/',views.login),
    # url(r'^code/',views.code),
    # url(r'^admin/',include(admin.site.urls)),
]
urlpatterns += staticfiles_urlpatterns()