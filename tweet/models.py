from django.db import models
from django.utils import timezone
from twitteruser.models import TwitterUser


class Tweet(models.Model):
    date = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=140)
    popularity = models.IntegerField(default=0)
    author = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
