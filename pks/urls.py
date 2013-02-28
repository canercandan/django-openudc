from django.conf.urls.defaults import *
from django.views.generic import TemplateView

urlpatterns = patterns('pks.views',
                       url(r'^$', 'index'),
                       url(r'^add$', 'add'),
                       url(r'^lookup$', 'lookup'),
                       url(r'^ok$', TemplateView.as_view(template_name='pks/ok.html')),
                       )
