from django.conf.urls import patterns, url

urlpatterns = patterns('api.views_set.views_watch',

    url(r'^add_watchers/$', 'add_watchers'),
    url(r'^remove_watcher/$', 'remove_watcher'),
    url(r'^get_updated_watch_list/$', 'get_updated_watch_list'),

)dd