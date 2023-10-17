from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from .manager import UserManager

class User(AbstractUser):
    username = None
    email=models.EmailField(unique=True)
    is_varified=models.BooleanField(default=False)
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS=[]
    objects=UserManager()
    def name(self):
        return self.first_name+' '+self.last_name
    def __str__(self):
        return self.email

