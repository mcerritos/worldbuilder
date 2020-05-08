from django.forms import ModelForm
from .models import Project, Post, Picture

class ProjectForm(ModelForm):
  class Meta:
    model = Project
    fields = ['name', 'description', 'current']

class PostForm(ModelForm):
  class Meta:
    model = Post
    fields = ['text', 'title']

class PictureForm(ModelForm):
  class Meta:
    model= Picture
    fields =['image', 'project', 'user']

