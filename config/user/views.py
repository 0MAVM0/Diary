from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser
from django.views import View
from .forms import *

def home_page(request):
    return render(request, "home.html")

'''
def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration was successfull")

            return redirect("log_in")
    else:
        form = UserCreationForm()
    
    context = { "form" : form }

    return render(request, "user/signup.html", context)
'''

class SignUpView(View):
    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration was successful")

            return redirect("log_in")

        context = { "form" : form }

        return render(request, "user/sign_up.html", context)

    def get(self, request):
        form = UserCreationForm()

        context = { "form" : form }

        return render(request, "user/sign_up.html", context)

def log_in(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                return redirect("home")
            else:
                form.add_error(None, "Doesn't Exist")
    else:
        form = UserLoginForm()
    
    context = { "form" : form }

    return render(request, "user/log_in.html", context)

'''
class LogInView(View):
    def post(self, request):
        form = UserLoginForm(request.POST)

        if form.is_valid():
            return redirect("home")

        context = { "form" : form }

        return render(request, "user/log_in.html", context)
    
    def get(self, request):
        form = UserLoginForm()

        context = { "form" : form }

        return render(request, "user/log_in.html", context)
'''

def log_out(request):
    if request.method == "POST":
        logout(request)

        return redirect("log_in")
    return render(request, "user/log_out.html", {})
