# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from djangoProject.decorators import my_login_required
from djangoProject.utils import main_render


@my_login_required
def index(request):
    home(request)


@my_login_required
def home(request):
    context = {'segment': 'index'}

    return main_render(request,
                       "home.html",
                       context,
                       'home')
