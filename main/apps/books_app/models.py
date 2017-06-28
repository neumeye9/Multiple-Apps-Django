# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Books (models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    published_date=models.CharField(max_length=100)
    category= models.CharField(max_length=100)
    created_at= models.DateTimeField(auto_now_add= True)
    updated_at=models.DateTimeField(auto_now=True)
    in_print= models.BooleanField(default = True)
