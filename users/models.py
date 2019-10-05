from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # name = models.CharField(blank=True, max_length=255)
    avatar = models.ImageField(upload_to='user/pictures', blank=True, null=True)
    # first_name = models.CharField(blank=True,max_length=255)
    # last_name = models.CharField(blank=True,max_length=255)
    phone_number = models.IntegerField(default=0)
    CP = models.CharField(blank=True,max_length=40)
    Mesero = models.BooleanField(default=False)
    # streetAddress = models.CharField(max_length=40)
    # created = models.DateTimeField(auto_now_add=True)
    # modified = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.email