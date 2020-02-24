from django import forms
from .models import CustomUser

class LoginForm(forms.Form):
    username = forms.CharField(max)