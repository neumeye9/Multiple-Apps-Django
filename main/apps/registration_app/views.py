from django.shortcuts import render, redirect
from models import Users
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, 'registration_app/index.html')

def register(request):

    check = Users.usersManager.add(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['password'], request.POST['confirmpass'])
    print check 

    if check[0] == False:
        for message in check[1]:
            messages.add_message(request, messages.ERROR, message)
        return redirect('/')
    else:
        return redirect('/courses')


def login(request):

    check = Users.usersManager.enter(request.POST['logemail'], request.POST['logpassword'])

    if check[0] == False:
        for message in check[1]:
            messages.add_message(request, messages.ERROR, message)
            return redirect('/')
    else:
        request.session['userid'] = check[1].id
        print request.session['userid']
        request.session['username'] = check[1].first_name
        return redirect('/courses')

def success(request):
    messages.add_message(request, messages.SUCCESS, "You successfully registered/logged in!")

    return render(request, 'registration_app/success.html')