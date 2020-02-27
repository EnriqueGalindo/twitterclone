from django.shortcuts import render, redirect, reverse
from .models import Tweet
from .forms import TweetForm
from django.contrib.auth.decorators import login_required


@login_required()
def tweet_view(request):
    html = 'genericForm.html'

    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Tweet.objects.create(
                text=data["tweet"],
                author=request.user
                )
            return redirect(reverse("home"))
    form = TweetForm()
    return render(request, html, {'form': form})


def tweets_list_view(request):
    tweets = Tweet.objects.all()
    return render(request, 'tweets.html', {"tweets": tweets})
