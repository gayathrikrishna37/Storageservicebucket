# models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from datetime import datetime
import pytz
from django.contrib.auth.models import User


class UserCredentials(models.Model):
    userid = models.IntegerField()
    username = models.CharField(max_length=150)
    email = models.EmailField()
    
class UserData(models.Model):
    userid = models.IntegerField()
    bucketid = models.IntegerField()
    data = models.TextField()

    def __str__(self):
        return f"User {self.userid}, Bucket {self.bucketid}"