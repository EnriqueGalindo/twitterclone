from django.shortcuts import render, redirect, reverse
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from notification.models import Notification
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

# @login_required(login_url='/login/')
# def index_view(request):
#     current_user = TwitterUser.objects.filter(username=request.user.username)
#     following = request.user.user_follows.all()
#     user_pool = current_user | following
#     user = TwitterUser.objects.all()
#     tweets = Tweet.objects.filter(author=current_user.first())
#     tweet = Tweet.objects.filter(author__in=user_pool)
#     tweet_count = len(tweets)
#     follow_count = len(following)
#     notification_count = Notification.objects.filter(target_user=request.user).exclude(viewed=True).count()
#     return render(request,
#                   'index.html',
#                   {
#                       'user': user,
#                       'data': tweet,
#                       'tweet_count': tweet_count,
#                       'follow_count': follow_count,
#                       'notification_count': notification_count
#                   }
#                   )


class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        current_user = TwitterUser.objects.filter(username=request.user.username)
        following = request.user.user_follows.all()
        user_pool = current_user | following
        user = TwitterUser.objects.all()
        tweets = Tweet.objects.filter(author=current_user.first())
        tweet = Tweet.objects.filter(author__in=user_pool)
        tweet_count = len(tweets)
        follow_count = len(following)
        notification_count = Notification.objects.filter(target_user=request.user).exclude(viewed=True).count()

        return render(request,
                      'index.html',
                      {
                        'user': user,
                        'data': tweet,
                        'tweet_count': tweet_count,
                        'follow_count': follow_count,
                        'notification_count': notification_count
                      }
                      )
