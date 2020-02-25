from django import forms
from .models import Tweet


class TweetForm(forms.Form):
    tweet = forms.CharField(max_length=140)
