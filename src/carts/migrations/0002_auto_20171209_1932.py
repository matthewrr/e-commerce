# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 19:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Card',
            new_name='Cart',
        ),
    ]
