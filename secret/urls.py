from django.conf.urls import patterns, include, url
from django.contrib import admin
from recommendation import views



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'secret.views.home', name='home'),
    # url(r'^blog/', include('blog.urls'))
    url(r'^$', include("portal.urls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$',views.login,name='login'),
    url(r'^album/',include("album.urls")),
    url(r'^recommendation/',include("recommendation.urls")),
    url(r'^doc/',include("doc.urls")),
    url(r'^count/',include("count.urls")),
    url(r'^blog/',include("blog.urls"))
)
