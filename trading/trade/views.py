from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def product(request, pk):
    pass

def login_user(request):
    pass

def logout_user(request):
    pass

def register_user(request):
    pass

