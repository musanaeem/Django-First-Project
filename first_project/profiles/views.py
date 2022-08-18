from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages

from . models import *
from profiles.templates.forms import CreateUserForm

def index(request):
    return render(request, "profiles/index.html")

def register_page(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for" + user)
            return redirect("login")


    context = {"form":form}
    return render(request, "profiles/register.html", context)

def login_page(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username,password=password)
        context = {
            "user":username
        }
        if user is not None:
            login(request, user)
            return redirect("profiles/index", context)
        else:
            messages.info(request, "Username or Password is incorrect")
        
    context = {}
    return render(request, "profiles/login.html")

def logout_user(request):
    logout(request)
    return redirect("login")