#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView

from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from profiles.routers import router as profiles_router
from bundles.routers import router as bundles_router
from search.routers import router as search_router
from profiles import views
from matching.views import FlowerProxyHandler, MatchingMdeView


admin.autodiscover()

urlpatterns = patterns(
    '',

    # Tech

    # Admin panel and documentation:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()

