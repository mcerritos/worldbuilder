from django.forms import ModelForm
from .models import Project, Post, Question

class ProjectForm(ModelForm):
  class Meta:
    model = Project
    fields = ['name', 'description', 'current']

class PostForm(ModelForm):
  class Meta:
    model = Post
    fields = ['text', 'title']

