from django.conf.urls import patterns, url

urlpatterns = patterns('api.views_set.views_todo_list',

    url(r'^get_todo_list/$', 'get_todo_list'),
    url(r'^add_action/$', 'add_action'),
    url(r'^update_action/$', 'update_action'),
    url(r'^remove_action/$', 'remove_action'),
    url(r'^update_status/$', 'update_status'),
    url(r'^complete/$', 'complete'),

    url(r'^add_project/$', 'add_project'),
    url(r'^get_all_projects/$', 'get_all_projects'),

    url(r'^get_updated_info/$', 'get_updated_info'),

)