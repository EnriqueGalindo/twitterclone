from django.db import models
from django.utils import timezone

class Tweet(models.Model):
    date = models.DateTimeField(defaulttimezone.now)
    Text = models.CharField(max_length=140)
    popularity = models.IntegerField(default=0)
