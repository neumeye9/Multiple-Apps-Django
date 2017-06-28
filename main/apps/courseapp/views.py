# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from .models import Course

def index(request):
    context = {
    "courses" : Course.objects.all()
    }
    return render(request, 'courseapp/index.html', context)

def courses(request):
    if request.method == "POST":
        Course.objects.create(name = request.POST['name'], description = request.POST['description'])
        return redirect('/')
    else:
        return redirect('/')

def remove_confirm(request, id):
    course = Course.objects.get(id=id)
    context = {
    "course": course
    }
    return render(request, 'courseapp/remove.html', context)

def delete(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('/')

def logout(request):
    return redirect('/')
