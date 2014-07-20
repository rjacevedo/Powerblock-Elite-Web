from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', 'PbElite.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^testing/$', 'PbElite.views.sendPD'),
    url(r'^testing/(?P<login>[0-9]+)/(?P<circuitNum>[0-9]+)/(?P<value>[0-1])/$', 'PbElite.views.sendPD'), 
    url(r'^circuits/(?P<login>[0-9]+)/$', 'PbElite.views.grabCircuits'),            
)
