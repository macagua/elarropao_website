import os.path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.defaults import *
from hitcount.views import update_hit_count_ajax

from elarropao.settings import PATH

admin.autodiscover()

urlpatterns = patterns('')

# Mis URL para mis APPS
urlpatterns += patterns('',
    (r'^$', 'elarropao.loteria.views.index'),
    (r'^loteria/', include('elarropao.loteria.urls')),
    (r'^sorteo/(\d{1,2})/$', 'elarropao.loteria.views.sorteo'),
    (r'^contacto/$', 'elarropao.loteria.views.contacto'),
)

urlpatterns += patterns('',
    (r'^admin/', include(admin.site.urls)),

    #Contador de visitas
    url(r'^ajax/hit/$', 
        update_hit_count_ajax,
        name='hitcount_update_ajax'),

    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/filebrowser/', include('filebrowser.urls')),
    #url(r'^newsletters/', include('emencia.django.newsletter.urls')),
    url(r'^newsletters/', include('emencia.django.newsletter.urls.newsletter')),
    url(r'^mailing/', include('emencia.django.newsletter.urls.mailing_list')),
    url(r'^tracking/', include('emencia.django.newsletter.urls.tracking')),
    url(r'^statistics/', include('emencia.django.newsletter.urls.statistics')),
)

urlpatterns += patterns('',
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(PATH, "site_media")}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
#        {'document_root': '/home/syra/proyectos/virtualenv/python2.5/lib/python2.5/site-packages/django/contrib/admin/media'}),
        {'document_root': '/home/lcaballero/Aplicaciones/virtualenv/python2.5/lib/python2.5/site-packages/django/contrib/admin/media'}),
)
