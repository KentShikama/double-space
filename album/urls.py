from django.conf.urls import patterns, url
from album import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'upload/$',views.upload,name='upload'),
)