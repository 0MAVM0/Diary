from django.core.exceptions import ValidationError
from .models import CustomUser
from django import forms

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords Are Not Matching To Each Other!")

        return password1

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=255, label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        user = CustomUser.objects.filter(username=username, password=password).first()

        if user:
            if not user.check_password(password):
                raise ValidationError("Password Is Not Correct")
        else:
            raise ValidationError("Not Exists")
        
        return self.cleaned_data
