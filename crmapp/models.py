from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.email

class Lead(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=20, null=True, blank=True)
    last_name=models.CharField(max_length=20, null=True, blank=True)
    age=models.IntegerField(default=0)
    image=models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

