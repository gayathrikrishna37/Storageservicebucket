# models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from datetime import datetime
import pytz
from django.contrib.auth.models import User
from django.utils import timezone


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
    
    
class Bucket(models.Model):
    bucket_name = models.CharField(max_length=100)
    description = models.TextField()
    bucket_type = models.CharField(max_length=50)
    bucket_id = models.IntegerField()
    creation_date = models.DateTimeField(default=timezone.now)  # Automatically set on creation
    updation_date = models.DateTimeField(default=timezone.now)      # Automatically updated on save

    def __str__(self):
        return self.bucket_name
