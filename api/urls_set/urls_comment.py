from django.conf.urls import patterns, url

urlpatterns = patterns('api.views_set.views_comment',

    url(r'^add_comment/$', 'add_comment'),
    url(r'^get_comment_list/$', 'get_comment_list'),
)