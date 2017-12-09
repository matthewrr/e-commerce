# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def cart_home(request):
    cart_id = request.session.get("card_id", None)
    if cart_id is None: #and isinstance(cart_id, int):
        print("Create new cart")
        request.session['card_id'] = 12
    else:
        print("Cart ID exists")
    return render(request, "carts/home.html", {})