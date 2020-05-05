from django.shortcuts import render, redirect
from .models import Project, Warfare, Culture, Government, Question, Post
from .forms import ProjectForm, PostForm

from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

################################# domain pages
def home(request):
      return render(request, 'homepage.html')


def culture(request):
  error_message=''
  #find the active project // find the culture associated with that object
  project_id = Project.objects.filter(users=request.user)[0]
  c = Culture.objects.get(project=project_id)

   # find all questions/posts associated with that domain
  questions = Question.objects.filter(culture=c).all()
  posts = Post.objects.filter(culture=c).all()

  if request.method == 'POST':
    post_form = PostForm(request.POST)
    if post_form.is_valid() :
      new_post = post_form.save()
      new_post.author_id = request.user.id
      c.posts.add(new_post)
      new_post.save()
      return redirect('culture')
    else:
      error_message = 'Something went wrong - please enter your post again.'
    
  else:
    post_form = PostForm()
  return render(request, 'domains/culture.html', {'questions' : questions, 'posts': posts, 'post_form': post_form,})

def geography(request):
    return render(request, 'domains/geography.html')

def government(request):
  error_message=''
  #find the active project // find the gov domain associated with that object
  project_id = Project.objects.filter(users=request.user)[0]
  gov = Government.objects.get(project=project_id)

   # find all questions/posts associated with that domain
  questions = Question.objects.filter(government=gov).all()
  posts = Post.objects.filter(government=gov).all()

  if request.method == 'POST':
    post_form = PostForm(request.POST)
    if post_form.is_valid() :
      new_post = post_form.save()
      new_post.author_id = request.user.id
      gov.posts.add(new_post)
      new_post.save()
      return redirect('government')
    else:
      error_message = 'Something went wrong - please enter your post again.'
    
  else:
    post_form = PostForm()
  return render(request, 'domains/government.html', {'questions' : questions, 'posts': posts, 'post_form': post_form,})

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
  
  # project creation if posted
  if request.method == 'POST':
    project_form = ProjectForm(request.POST)
    if project_form.is_valid() :
      new_project = project_form.save()
      new_project.users.add(request.user)
      new_project.save()

      #if project is active make all other projects from that user inactive
      if (new_project.current == True):
        other_projects = Project.objects.filter(users=request.user).exclude(id=new_project.id)
        for project in other_projects:
          project.current = False

      # create domains when project made
      Culture.objects.create(project=new_project)
      Warfare.objects.create(project=new_project)
      Government.objects.create(project=new_project)
      
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
      if new_project.current == True :
        other_projects = Project.objects.exclude(id=new_project.id)
        for project in other_projects:
          project.current = False
    return redirect('profile')
      
  else:
    form = ProjectForm(instance=project)
    
  return render(request, 'registration/profile.html', {'form': form})

##################### post delete and update

@login_required
def post_delete(request, post_id):
  ## post author is user.request
  this_post = Post.objects.get(id=post_id)
  if (this_post.author == request.user):
    Post.objects.get(id=post_id).delete()
  
  return redirect('profile')
