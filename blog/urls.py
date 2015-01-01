from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
    url(r'^$', views.all, name='all'),
    url(r'compose/$',views.compose,name="compose"),
    url(r'(?P<person>[A-Za-z]+)/$',views.person,name='person'),
    url(r'(?P<person>[A-Za-z]+)/(?P<article>[0-9]+)$',views.article,name="article"),
    url(r'(?P<person>[A-Za-z]+)/(?P<article>[0-9]+)/edit$',views.edit,name="edit"),
)