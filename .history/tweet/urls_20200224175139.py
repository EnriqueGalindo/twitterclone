from django.contrib import admin
from django.urls import path
from .forms import (
    tweet_view,
    like_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tweet/', tweet_view),
    path