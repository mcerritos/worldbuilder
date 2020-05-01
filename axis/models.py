from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length= 100)
    description = models.TextField(max_length= 500)
    users = models.ManyToManyField(User)
   
    def __str__(self):
        return self.name
