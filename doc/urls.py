from django.conf.urls import patterns, url
from doc import views

urlpatterns = patterns('',


    url(r'^$', views.display, name='display'),
    url(r'new/$',views.new, name='new'),

)
