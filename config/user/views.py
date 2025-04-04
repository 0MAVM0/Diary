from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import UserForm

def sign_up(request):
    form = UserForm

    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data["password1"])
            form.save()

            return redirect("home")
    else:
        form = UserForm()
    
    context = { "form" : form }

    return render(request, "user/signup.html", context)
