# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product

class SearchProductView(ListView):
    template_name = "search/view.html"
    
    def get_queryset(self, *args, **kwargs):
        request = self.request
        print(request.GET)
        query = request.GET.get('q')
        print(query)
        if query is not None:
            return Product.objects.filter(title__icontains=query)
        return Product.objects.featured()
        
        '''
        __icontains = field contains this (not case-sensitive)
        __iexact = field is exactly this
        '''