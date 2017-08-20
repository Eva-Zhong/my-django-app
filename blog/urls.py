from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^searchbyname/(?P<search_key>\w+)/$', views.post_search_title, name='post_search_title'),
	url(r'^searchbydpt/(?P<search_key>\w+)/$', views.post_search_dpt, name='post_search_dpt'),
	url(r'^post/$', views.post_index, name='post_index'),
]

