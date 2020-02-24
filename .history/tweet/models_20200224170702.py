from django.db import models


class Tweet(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    Text = models.CharField(max_length=140)
    popularity = models.IntegerField(def)
