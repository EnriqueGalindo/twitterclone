from twitteruser.models import TwitterUser
from django.http import HttpResponseRedirect
from tweet.models import Tweet
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from .forms import LoginForm, RegisterForm


def login_view(request):
    html = "genericForm.html"

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data["username"],
                                password=data["password"])
            if user:
                login(request, user)
                return redirect(request.GET.get("next", "/"))
            else:
                return HttpResponse("invalid authentication")

    form = LoginForm()

    return render(request, html, {'form': form})


def register_view(request):
    html = "genericForm.html"

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = TwitterUser.objects.create_user(
                username=data["username"],
                password=data["password"],
                display_name=data["display_name"]
            )
            login(request, user)
            return redirect(reverse("home"))

    form = RegisterForm()

    return render(request, html, {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def following_view(request, id):
    target_user = TwitterUser.objects.get(id=id)
    current_user = request.user
    current_user.user_follows.add(target_user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def user_view(request, id):
    user = TwitterUser.objects.get(id=id)
    tweets = Tweet.objects.filter(author=user)
    tweet_count = len(tweets)
    following = user.user_follows
    following_count = following.count()
    return render(request,
                  'user.html',
                  {
                        'target_user': user,
                        'tweets': tweets,
                        'tweet_count': tweet_count,
                        'following_count': following_count
                   }
                  )
