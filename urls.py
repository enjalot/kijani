from django.conf.urls.defaults import patterns, include, url
import arduino

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     #url(r'^$', 'bacteriabot.views.home', name='home'),
    # url(r'^bacteriabot/', include('bacteriabot.foo.urls')),
     url(r'^arduino/$', 'arduino.views.index',name='home'),
     url(r'^arduino/upload', 'arduino.views.upload',name='upload'),
     url(r'^arduino/latest', 'arduino.views.latest',name='latest'),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
