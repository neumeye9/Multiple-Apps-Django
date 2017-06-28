# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Books

def index(request):
    Books.objects.create(title= "Happy World", author= "Jenny", published_date="1984.05.23", category="Human")
    Books.objects.create(title= "Construction Management", author= "Jenny", published_date="2018", category="Education")
    Books.objects.create(title= "Leah", author= "Jenny and Grant", published_date="2011", category="Happy Life")
    Books.objects.create(title= "Lena", author= "Jenny and Grant", published_date="2014", category="Happy Life")
    Books.objects.create(title= "Coding World", author= "Jenny", published_date="May 2017", category="Education")
    Books.objects.create(title= "Lunch Time!", author= "Jenny", published_date="6.22.2017", category="Food")
    Books.objects.create(title= "Again?!", author= "Jenny", published_date="6.22.2017", category="Life")
    books= Books.objects.all()


    context= {
        "books":books
    }
    return render (request, 'books_app/index.html', context)
