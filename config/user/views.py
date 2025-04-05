from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from .models import CustomUser
from django.views import View
from .forms import UserCreationForm

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
            form.save()

            return redirect("login")

        context = { "form" : form }

        return render(request, "user/sign_up.html", context)

    def get(self, request):
        form = UserCreationForm()

        context = { "form" : form }

        return render(request, "user/sign_up.html", context)
