from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^search/(?P<search_key>\w+)/$', views.post_search, name='post_search'),
	url(r'^post/$', views.post_index, name='post_index'),
]

