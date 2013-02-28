from django.conf.urls.defaults import *
from django.views.generic import TemplateView

urlpatterns = patterns('peers.views',
                       url(r'^$', 'list'),
                       url(r'^list$', 'list'),
                       url(r'^register$', 'register'),
                       url(r'^ok$', TemplateView.as_view(template_name='peers/ok.html')),
                       )
