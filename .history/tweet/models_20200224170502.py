from django.db import models

class Tweet(models.Model):
    date = models.DateTimeField()
