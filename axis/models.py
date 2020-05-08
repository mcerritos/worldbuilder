from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

POSITIONS = (
    ('Sum', 'Summary'),
    ('Shd', 'Section Header'),
    ('Ssc', 'Subsection')
)

class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length= 500, default="Describe your project here.")
    users = models.ManyToManyField(User)
    current = models.BooleanField(default=False)
   
    def __str__(self):
        return self.name

class Question(models.Model):
    text = models.TextField(max_length=250)
    display = models.BooleanField(default=True)
    domain = models.TextField(default="Miscellaneous")

class Post(models.Model):
    title= models.CharField(max_length=150)
    author= models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
    text = models.TextField(max_length=2000)
    position = models.CharField(
        max_length=3,
        choices=POSITIONS,
        default=POSITIONS[2][0])
    
    def __str__(self):
        return self.title + " by " + self.author.username 

class Picture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    domain = models.TextField(default="Miscellaneous")

#### profile class 
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
    title: models.CharField(max_length=200)
    summary: models.TextField(max_length=500)
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

class Geography(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    navbar = models.BooleanField(default=True)
    questions = models.ManyToManyField(Question)
    posts = models.ManyToManyField(Post)

class History(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    navbar = models.BooleanField(default=True)
    questions = models.ManyToManyField(Question)
    posts = models.ManyToManyField(Post)

