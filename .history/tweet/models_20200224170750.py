from django.db import models


class Tweet(models.Model):
    date = models.DateTimeField(tim)
    Text = models.CharField(max_length=140)
    popularity = models.IntegerField(default=0)
