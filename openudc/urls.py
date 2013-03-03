from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView, TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Uncomment the admin/doc line below to enable admin documentation
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       # Uncomment the next line to enable the admin
                       url(r'^admin/', include(admin.site.urls)),

                       url(r'^$', 'openudc.views.home', name='home'),
                       url(r'^capabilities$', 'openudc.views.capabilities', name='capabilities'),
                       url(r'^pks/', include('pks.urls')),
                       url(r'^peers/', include('peers.urls')),
                       )
