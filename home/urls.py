# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from django.views.generic.base import RedirectView

from home import views

urlpatterns = [
    path('home', views.home, name='home'),
    re_path(r'^.*$', RedirectView.as_view(url='home', permanent=False), name='index')
]
