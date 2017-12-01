# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
import os
from django.db import models
from django.db.models.signals import pre_save

from .utils import unique_slug_generator

def get_filename_ext(filename):
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(base_name)
    return name, ext

#makes sure there's no issue with uploading files.
#For example, could have spaces in URL. Could name off of title, etc. instead.
def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1,3759237)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    #3.6 allows final_filename = f'{new_filename}{ext}'
    return "products/{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename
        )

class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)
    
    def featured(self):
        return self.filter(featured=True, active=True)

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)
    
    def all(self): #also makes call to ProductQuerySet like fcn below
        return self.get_queryset().active()
        #will exclude objects marked inactive
    
    def featured(self):
        return self.get_queryset().featured()
    #.featured() == filter(featured=True). The idea is that we can
    #get_queryset() then pass through ProductQuerySet to filter
    
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id) #Product.objects same-ish
        if qs.count() == 1:
            return qs.first()
        return None

# Create your models here. Almost always name in singular.
class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=10,default=39.99) 
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    
    objects = ProductManager()
    #null not default allows non-values in DB.
    #blank means not required in Django (i.e. admin will be chill)
    
    def get_absolute_url(self):
        return "/products/{slug}".format(slug=self.slug)
    
    def __str__(self):
        return self.title #python 3
    
    def __unicode__(self):
        return self.title #python 2

def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)