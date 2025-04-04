from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import CustomUser
from django.views import View
from .forms import *

def home_page(request):
    return render(request, "home.html")

'''
def sign_up(request):
    form = UserCreationForm

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data["password1"])
            form.save()

            return redirect("login")
    else:
        form = UserCreationForm()
    
    context = { "form" : form }

    return render(request, "user/signup.html", context)
'''

class SignUpView(View):
    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data["password1"])
            user.save()

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
                form.add_error("Doesn't Exist")
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
