from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length= 100)
    description = models.TextField(max_length= 500)
    users = models.ManyToManyField(User)
    current = models.BooleanField(default=False)
   
    def __str__(self):
        return self.name

class Question(models.Model):
    text = models.TextField(max_length=250)
    display = models.BooleanField(default=True)

class Post(models.Model):
    text = models.TextField(max_length=2000)
    author= models.ForeignKey(User, on_delete=models.SET_DEFAULT, default="Anonymous")
    title= models.CharField(max_length=150)

class Culture(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    navbar =models.BooleanField(default=True)
    questions = models.ManyToManyField(Question)
    posts = models.ManyToManyField(Post)

class Warfare(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    navbar =models.BooleanField(default=True)
    questions = models.ManyToManyField(Question)
    posts = models.ManyToManyField(Post)

class Government(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    navbar =models.BooleanField(default=True)
    questions = models.ManyToManyField(Question)
    posts = models.ManyToManyField(Post)

