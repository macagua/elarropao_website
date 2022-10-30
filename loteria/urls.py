#!/usr/bin/env python
from django.conf.urls.defaults import *
import os.path
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^triples/$', 'elarropao.loteria.views.triples'),
    (r'^otros/$', 'elarropao.loteria.views.otros'),
)
