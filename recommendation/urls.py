from django.conf.urls import patterns, url
from recommendation import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'thread/(?P<thread_id>\d+)/$',views.thread,name="thread"),
    url(r'category/(?P<category_name>[a-z]+)/$',views.category,name="category")
)