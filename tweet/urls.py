from django.urls import path
from .views import (
    tweet_view,
    tweets_list_view
)

urlpatterns = [
    path('tweet/', tweet_view),
    path('tweets/', tweets_list_view)
]
