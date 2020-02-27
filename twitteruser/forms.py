from django import forms
from .models import TwitterUser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20)
    display_name = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
