from __future__ import unicode_literals
from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-


from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TwitterCredentails(models.Model):
    #related_name it is used to do the indexing on foreing key. it gives the reverse relation on a query
    #user = models.ForeignKey(User, related_name="credentials', on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name="credentials",on_delete=models.CASCADE)
    access_token = models.CharField(max_length=100,null=True)
    access_secret = models.CharField(max_length=100,null=True)
    consumer_key = models.CharField(max_length=100,null=True)
    consumer_secret = models.CharField(max_length=100,null=True)



