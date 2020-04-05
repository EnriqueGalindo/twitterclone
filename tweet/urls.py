from django.urls import path
from .views import (
    tweet_view,
    # tweets_list_view,
    TweetListView
)

urlpatterns = [
    path('tweet/', tweet_view),
    path('tweets/', TweetListView.as_view())
]
