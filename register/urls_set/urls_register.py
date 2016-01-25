from django.conf.urls import patterns, url

urlpatterns = patterns('register.views_set.views_register',

    url(r'^register/$', 'register'),
    url(r'^login/$', 'login'),
    url(r'^logout/$', 'logout'),

)