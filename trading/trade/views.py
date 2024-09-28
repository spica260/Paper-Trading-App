from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Product
from django.contrib import messages
from .forms import SignUpForm
import requests
import json

def home(request):
    products = Product.objects.all()
    ticker = 'ELF'
    api_request = requests.get("https://api.marketstack.com/v1/eod?access_key=6fdf201f00373afd80eb7d2c2efea784&date_from=2024-08-01&date_to=2024-08-03&symbols=" + ticker)
    api = json.loads(api_request.content)
    stock_data = api['data']

    return render(request, 'home.html', {'products': products, 'stock_data': stock_data})

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
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("You have been register successfully."))
            return redirect('home')
        else:
            messages.success(request, ("There is an error registering, please try again."))
            return redirect('register')
    else:
        return render(request, 'register.html', {'form':form})

