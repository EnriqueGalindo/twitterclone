from django import forms


class TweetForm(forms.Form):
    tweet = forms.CharField(max_length=)