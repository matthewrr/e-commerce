# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from carts.models import Cart

ORDER_STATUS_CHOICES = (
    ('create', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded'),
)
    #finding first element and displaying second

class Order(models.Model):
    order_id = models.CharField(max_length=120, blank=True)
    # billing_profile = 
    # shipping_address = 
    # billing_address =
    cart = models.ForeignKey(Cart)
    status = models.CharField(max_length=120, default='created', choices=ORDER_STATUS_CHOICES)
    shipping_total = models.DecimalField(default=5.99, max_digits=100, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

    def __str__(self):
        return self.order_id