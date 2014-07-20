from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', 'PbElite.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^testing/$', 'PbElite.views.sendPD'),
    url(r'^testing/(?P<value>\d+)/$', 'PbElite.views.sendPD'),                   
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/sendReading', 'PbElite.views.getReading'),
)

