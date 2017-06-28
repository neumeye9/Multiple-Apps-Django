from __future__ import unicode_literals

from django.db import models

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
Name_REGEX = re.compile(r'^[a-zA-Z]+$')

# Create your models here.

class UsersManager(models.Manager):
    def add(self,first_name,last_name,email,password,confirmpass):
       
        messages = []

        if len(first_name) == 0:
            messages.append('First Name is required.')
        if len(first_name) < 2:
            messages.append('First Name must be longer than two characters')
        if not first_name.isalpha():
            messages.append('First Name can only contain letters')
        if len(last_name) == 0:
            messages.append('Last Name is required')
        if len(last_name) < 2:
            messages.append('Last Name must be longer than two characters')
        if not last_name.isalpha():
            messages.append('Last Name can only contain letters')
        if len(email) < 1:
            messages.append('Email is required to register.')
        if not EMAIL_REGEX.match(email):
            messages.append('Not a valid Email Address')
        if len(email) > 1:
            check = Users.usersManager.filter(email=email)
            if len(check) > 0:
                messages.append('Email already taken')
        if len(password) < 1:
            messages.append('Password is required to register')
        if len(password) < 8:
            messages.append('Password must be at least 8 characters long')
        if len(confirmpass) == 0:
            messages.append('Password Confirmation is required')
        if password != confirmpass:
            messages.append('Password and Password confirmation do not match')


        
        if len(messages) > 0:
            return False, messages
        else:
            user = Users.usersManager.create(first_name=first_name, last_name=last_name,email=email,password=password)
            return(True, user)
        

    def enter(self,logemail,logpassword):

        messages = []
        
        user = Users.usersManager.filter(email=logemail)

        if len(logemail) == 0:
            messages.append('You must enter an email to login')
        if not EMAIL_REGEX.match(logemail):
            messages.append('Email entered is not a valid email address')
        if len(user) < 1:
           messages.append('User does not exist, please register')
        if logpassword != user[0].password:
            messages.append('Password does not match user, please reenter.')

        if len(messages) > 0:
            return False, messages
        
        else:
            return (True, user[0])
             

class Users(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    usersManager = UsersManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



