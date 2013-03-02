from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView, TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from udid2 import Udid2
__keys__ = [x for x in Udid2.HashedVerboseParser()()]

urlpatterns = patterns('',
                       # Examples
                       url(r'^$', 'openudc.views.home', name='home'),
                       url(r'^capabilities$', 'openudc.views.capabilities', name='capabilities'),

                       # url(r'^openudc/', include('openudc.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin
                       url(r'^admin/', include(admin.site.urls)),
                       # url(r'^polls/', include('polls.urls')),
                       # url(r'^pgpauth/', include('pgpauth.urls')),
                       # url(r'^books/', include('books.urls')),
                       url(r'^pks/', include('pks.urls')),
                       url(r'^peers/', include('peers.urls')),
                       )
