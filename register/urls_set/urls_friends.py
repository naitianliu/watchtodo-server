from django.conf.urls import patterns, url

urlpatterns = patterns('register.views_set.views_friends',

    url(r'^get_friend_list/$', 'get_friend_list'),
    url(r'^get_user_list_by_keyword/$', 'get_user_list_by_keyword'),
    url(r'^send_friend_request/$', 'send_friend_request'),
    url(r'^accept_friend_request/$', 'accept_friend_request'),
    url(r'^get_pending_friend_request_list/$', 'get_pending_friend_request_list'),

)