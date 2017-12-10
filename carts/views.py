# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Cart

def cart_home(request):
    cart_obj = Cart.objects.new_or_get(request)
    return render(request, "carts/home.html", {})