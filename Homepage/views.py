
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Destination


def home(request):

    dest = Destination.objects.all()
    return render(request, 'index.html', {'dests': dest})


def refresh(request):
    dest = Destination.objects.all()
    return render(request, 'index.html', {'dests': dest})


def signup(request):

    if request.method == 'POST':
        fullname = request.POST['fullname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pass']
        password2 = request.POST['pass2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exits')
                return redirect('/signup')

            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exits')
                return redirect('/signup')
            else:
                user = User.objects.create_user(name=fullname, username=username, email=email, password=password)
                user.save()
                return redirect('/')
        else:
            messages.info(request, 'password not matched')
            return redirect('/signup')

    else:
        return render(request, 'signup.html')


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['pass']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/refresh')
        else:
            messages.info(request, 'Invalid user')
            return render(request, 'sign_in.html')
    else:
        return render(request, 'sign_in.html')


def signout(request):
    auth.logout(request)
    return redirect('/')