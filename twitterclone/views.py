from django.shortcuts import render, redirect, reverse
from twitteruser.models import TwitterUser
from tweet.models import Tweet


def index_view(request):
    user = TwitterUser.objects.all()
    tweet = Tweet.objects.all()
    return render(request,
                  'index.html',
                  {'user': user, 'tweet': tweet}
                  )



