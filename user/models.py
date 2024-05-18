from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from user.manager import UserManager 
from random import randint

class User(AbstractBaseUser,PermissionsMixin) : 
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False) 
    joind = models.DateTimeField(auto_now_add=True)
    otp = models.SlugField(null=True,blank=True,max_length=6)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()
    
    def __str__(self) : 
        return str(self.email)
    
    def save(self,*args,**kwargs): 
        self.otp = randint(100000,999999)
        return super().save(*args,**kwargs)