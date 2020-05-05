from django.contrib import admin
from .models import Project, Post, Question, Culture, Warfare, Government

# Register your models here.
admin.site.register(Project)
admin.site.register(Post)
admin.site.register(Question)
admin.site.register(Culture)
admin.site.register(Warfare)
admin.site.register(Government)