from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Project(models.Model):
    name = models.CharField(max_length=100, default="Give your project a name!")
    description = models.TextField(max_length= 500, default="Describe your project here.")
    users = models.ManyToManyField(User)
    current = models.BooleanField(default=False)
   
    def __str__(self):
        return self.name

class Question(models.Model):
    text = models.TextField(max_length=250)
    display = models.BooleanField(default=True)

class Post(models.Model):
    text = models.TextField(max_length=2000)
    author= models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
    title= models.CharField(max_length=150)

    def __str__(self):
        return self.title + " by " + self.author.username 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    current_project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

##### domain models 

class Culture(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    navbar =models.BooleanField(default=True)
    questions = models.ManyToManyField(Question)
    posts = models.ManyToManyField(Post)

class Warfare(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    navbar = models.BooleanField(default=True)
    questions = models.ManyToManyField(Question)
    posts = models.ManyToManyField(Post)

class Government(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    navbar = models.BooleanField(default=True)
    questions = models.ManyToManyField(Question)
    posts = models.ManyToManyField(Post)

class Religion(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    navbar = models.BooleanField(default=True)
    questions = models.ManyToManyField(Question)
    posts = models.ManyToManyField(Post)

