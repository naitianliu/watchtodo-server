"""watchtodo URL Configuration

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

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'register.views_set.views_register.version'),

    url(r'^auth/', include('register.urls_set.urls_register')),
    url(r'^friends/', include('register.urls_set.urls_friends')),

    url(r'^todo/', include('api.urls_set.urls_todo_list')),
    url(r'^watch/', include('api.urls_set.urls_watch')),
    url(r'^comment/', include('api.urls_set.urls_comment')),
    url(r'^watch/', include('api.urls_set.urls_watch')),
]
