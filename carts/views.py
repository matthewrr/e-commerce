# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Cart

def cart_create(user=None):
    cart_obj = Cart.objects.create(user=None)
    print("New cart created")
    return cart_obj

def cart_home(request):
    request.session['cart_id'] = "12"
    cart_id = request.session.get('card_id', None)
    # if cart_id is None:
    #     cart_obj = cart_create()
    #     request.session['card_id'] = cart_obj.id
    # else:
    qs = Cart.objects.filter(id=cart_id)
    if qs.count() == 1:
        print("Cart ID exists")
        cart_obj = qs.first()
    else:
        cart_obj = cart_create()
        request.session['card_id'] = cart_obj.id
    return render(request, "carts/home.html", {})