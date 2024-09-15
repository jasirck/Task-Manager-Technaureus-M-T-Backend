from django.db import models
from django.contrib.auth.models import AbstractUser

# New AbstractUser for customizing the user model
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, null=False) 
    username = models.CharField(max_length=150, unique=True, null=False)  

# Task manager table structure
class Task(models.Model):
    title = models.CharField(max_length=255,null=False)
    description = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title