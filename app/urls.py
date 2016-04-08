#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView

from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


admin.autodiscover()

urlpatterns = patterns(
    '',

    # Tech

    # Admin panel and documentation:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
