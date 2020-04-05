from django.shortcuts import render, redirect, reverse
from .models import Tweet
from .forms import TweetForm
from notification.models import Notification
from twitteruser.models import TwitterUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


@login_required()
def tweet_view(request):
    html = 'genericForm.html'

    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tweet = Tweet.objects.create(
                text=data["tweet"],
                author=request.user
                )
            for word in data["tweet"].split(" "):
                if word.startswith("@"):
                    username = word[1:]
                    users = TwitterUser.objects.filter(username=username)
                    if users.exists():
                        Notification.objects.create(
                            target_user=users.first(),
                            tweet=tweet
                        )
            return redirect(reverse("home"))
    form = TweetForm()
    return render(request, html, {'form': form})

# @login_required(login_url='/login/')
# def tweets_list_view(request):
#     tweets = Tweet.objects.all()
#     return render(request, 'tweets.html', {"tweets": tweets})


class TweetListView(LoginRequiredMixin, View):
    def get(self, request):
        html = 'tweets.html'
        tweets = Tweet.objects.all()
        return render(request, html, {'tweets': tweets})
