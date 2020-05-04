from django.shortcuts import render, redirect
from .models import Project, Warfare, Culture, Question, Post
from .forms import ProjectForm

from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

################################# domain pages
def home(request):
      return render(request, 'homepage.html')

def culture(request):
  #find the active project // find the culture associated with that object
  project_id = Project.objects.get(users=request.user)
  c = Culture.objects.get(project=project_id)

   # find all questions/posts associated with that domain
  questions = Question.objects.filter(culture=c).all()
  posts = Post.objects.filter(culture=c).all()
  return render(request, 'domains/culture.html', {'questions' : questions, 'posts': posts})

def geography(request):
    return render(request, 'domains/geography.html')

def government(request):
    return render(request, 'domains/government.html')

def history(request):
    return render(request, 'domains/history.html')

def religion(request):
    return render(request, 'domains/religion.html')

def warfare(request):
  project_id = Project.objects.get(users=request.user)
  w = Warfare.objects.get(project=project_id)

  # find all questions/posts associated with that domain
  questions = Question.objects.filter(warfare=w).all()
  posts = Post.objects.filter(warfare=w).all()
  return render(request, 'domains/warfare.html', {'questions' : questions, 'posts': posts} )

################################### auth routes 
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

#################################### project crud + profile
@login_required
def profile(request):
  error_message = ''
  projects = Project.objects.filter(users=request.user)
  
  if request.method == 'POST':
    project_form = ProjectForm(request.POST)
    if project_form.is_valid() :
      new_Project = project_form.save()
      new_Project.users.add(request.user)
      new_Project.save()
      return redirect('profile')
    else:
      error_message = 'Invalid project - try again'
    
  else:
    project_form = ProjectForm()
  
  return render(request, 'registration/profile.html', { 'projects': projects, 'project_form': project_form, 'error_message': error_message })

# def project_details(request, project_id):
# 	project = Project.objects.get(id=project_id)
# 	project_form = ProjectForm()
# 	return render(request, 'project_details.html', {'trip': trip, 'things': things, 'city': city })

@login_required
def project_delete(request, project_id):
	Project.objects.get(id=project_id).delete()
	return redirect('profile')

@login_required
def project_update(request, project_id):
	project = Project.objects.get(id=project_id)

	if request.method == 'POST':
		form = ProjectForm(request.POST, instance=project)
		if form.is_valid():
			new_project = form.save()
			return redirect('profile')
      
	else:
		form = ProjectForm(instance=project)

	return render(request, 'registration/profile.html', {'form': form})
