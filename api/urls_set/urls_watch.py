from django.conf.urls import patterns, url

urlpatterns = patterns('api.views_set.views_watch',

    url(r'^add_watcher/$', 'add_watcher'),
    url(r'^remove_watcher/$', 'remove_watcher'),
    url(r'^get_updated_watch_list/$', 'get_updated_watch_list'),

)