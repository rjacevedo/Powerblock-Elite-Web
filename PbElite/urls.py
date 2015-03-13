from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', 'PbElite.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'PbElite.views.grabLogin'),
    url(r'^home/$', 'PbElite.views.grabHomepage'),
    url(r'^updateCircuit/(?P<login>[0-9]+)/(?P<circuitNum>[0-9]+)/(?P<value>[0-1])/$', 'PbElite.views.updateCircuit'), 
    url(r'^circuits/(?P<login>[0-9]+)/$', 'PbElite.views.grabCircuits'),            
    url(r'^testing/(?P<value>\d+)/$', 'PbElite.views.sendPD'),                   
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/sendReading', 'PbElite.views.getReading'),
    url(r'^api/testResponse/(?P<rpid>\d+)/$', 'PbElite.views.test_response'),
    url(r'^api/grabReadings/(?P<login>[0-9]+)/$', 'PbElite.views.grabReadings'),
    url(r'^loginRequest/', 'PbElite.views.loginRequest'), 
    url(r'^account/', 'PbElite.views.grabAccount'),
    url(r'^schedule/', 'PbElite.views.grabSchedule'),
    url(r'^register/', 'PbElite.views.grabRegistration'),
    url(r'^api/registerNewUser/', 'PbElite.views.registerUser'),
    url(r'^api/getUserData/', 'PbElite.views.getUserData'),
    url(r'^api/updateUserData/', 'PbElite.views.updateUserData'),
    url(r'^api/newCalenderEvent/', 'PbElite.views.postNewEvent'),
    url(r'^api/getCalendarEvents/', 'PbElite.views.retrieveEvents'),
    url(r'^api/getCircuitData/', 'PbElite.views.getChartData'),
    url(r'^api/addARoom/', 'PbElite.views.addARoom'),
    url(r'^api/deleteARoom/', 'PbElite.views.deleteARoom'),
    url(r'^api/updateSchedule/', 'PbElite.views.updateSchedule'),
    url(r'^logout/', 'PbElite.views.logout'),
    url(r'^test/', 'PbElite.views.schedule'),
    url(r'^api/deleteSchedule', 'PbElite.views.deleteSchedule'),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()

