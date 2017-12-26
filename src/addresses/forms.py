# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from .models import Address

class AddressForm(forms.ModelForm):
    class Meta
        model = Address