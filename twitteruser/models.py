from django.db import models
from django.contrib.auth.models import AbstractUser


class TwitterUser(AbstractUser):
    user_follows = models.ManyToManyField('self',
                                          related_name='following',
                                          symmetrical=False
                                          )
    display_name = models.CharField(max_length=20, unique=True)
