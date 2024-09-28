from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'home.html')

def product(request, pk):
    pass

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, ("You're log in."))
            return redirect('home')
        else:
            messages.success(request, ("There was an error, please try again."))
            return redirect('login')
        
    else:
        return render(request, 'log-in.html')

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been log out."))
    return redirect('home')

def register_user(request):
    pass

