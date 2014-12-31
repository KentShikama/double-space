from django.conf.urls import patterns, url
from count import views

urlpatterns = patterns('',
    url(r'^$', views.timeline, name='timeline'),
)