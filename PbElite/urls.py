from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', 'PbElite.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', 'PbElite.views.grabHomepage'),
    url(r'^updateCircuit/(?P<login>[0-9]+)/(?P<circuitNum>[0-9]+)/(?P<value>[0-1])/$', 'PbElite.views.updateCircuit'), 
    url(r'^circuits/(?P<login>[0-9]+)/$', 'PbElite.views.grabCircuits'),            
    url(r'^testing/(?P<value>\d+)/$', 'PbElite.views.sendPD'),                   
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/sendReading', 'PbElite.views.getReading'),
    url(r'^api/testResponse/(?P<login>[0-9]+)/$', 'PbElite.views.test_response'),
    url(r'^api/grabReadings/(?P<login>[0-9]+)/$', 'PbElite.views.grabReadings'),
)

