# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World. Trying out something new")

def test(request):
    return HttpResponse("Testing, Testing Something...")
