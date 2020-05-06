from django.shortcuts import render, redirect
from .models import Project, Profile, Warfare, Culture, Government, Religion, Question, Post
from .forms import ProjectForm, PostForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
      return render(request, 'homepage.html')

### functions to handle functionality that is the same across different routes

def handlePost(request, domain, d_name):
    post_form = PostForm(request.POST)
    if post_form.is_valid():
      new_post = post_form.save()
      new_post.author_id = request.user.id
      domain.posts.add(new_post)
      new_post.save()
      return redirect("domains/"+d_name+"/")
    else:
      return 'Something went wrong - please enter your post again.' 

def getCurrentProject(request):
  profile = Profile.objects.get(user=request.user)
  project_id = profile.current_project
  return project_id

def createNewProject(project_form, request, populated):
  if populated:
    new_project = project_form.save()
  else:
    new_project = Project.objects.create()
  
  new_project.users.add(request.user)
  new_project.save()
  # create domains when project made
  Culture.objects.create(project=new_project)
  Warfare.objects.create(project=new_project)
  Government.objects.create(project=new_project)
  Religion.objects.create(project=new_project)

  #get profile associated with user and set current project to the new project
  profile = Profile.objects.get(user=request.user)
  profile.current_project = new_project
  profile.save()
      
  return redirect('profile')

################################# domain pages
def culture(request):
  project_id = getCurrentProject(request)

  c = Culture.objects.get(project=project_id)
  questions = Question.objects.filter(culture=c).all()
  posts = Post.objects.filter(culture=c).all()

  if request.method == 'POST':
    handlePost(request, c, "culture")
  
  post_form = PostForm()
  context = {'questions' : questions, 'posts': posts, 'post_form': post_form}
  return render(request, 'domains/culture.html', context )

def government(request):
  project_id = getCurrentProject(request)
  gov = Government.objects.get(project=project_id)
  questions = Question.objects.filter(government=gov).all()
  posts = Post.objects.filter(government=gov).all()

  if request.method == 'POST':
    handlePost(request, gov, "government")
    
  post_form = PostForm()
  context = {'questions' : questions, 'posts': posts, 'post_form': post_form}
  return render(request, 'domains/government.html', context)

def history(request):
    return render(request, 'domains/history.html')

def religion(request):
  project_id = getCurrentProject(request)
  r = Religion.objects.get(project=project_id)
  questions = Question.objects.filter(religion=r).all()
  posts = Post.objects.filter(religion=r).all()

  if request.method == 'POST':
    handlePost(request, r, "religion")
  
  post_form = PostForm()
  context = {'questions' : questions, 'posts': posts, 'post_form': post_form}
  return render(request, 'domains/religion.html', context )

def geography(request):
    return render(request, 'domains/geography.html')

def warfare(request):
  project_id = getCurrentProject(request)
  w = Warfare.objects.get(project=project_id)
  questions = Question.objects.filter(warfare=w).all()
  posts = Post.objects.filter(warfare=w).all()

  if request.method == 'POST':
    handlePost(request, w, "warfare")
  
  post_form = PostForm()
  context = {'questions' : questions, 'posts': posts, 'post_form': post_form}
  return render(request, 'domains/warfare.html', context )

################################### auth routes 
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      project_form = ProjectForm()
      createNewProject(project_form, request, False)
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
      createNewProject(project_form, request, True)
    else:
      error_message = 'Invalid project - try again'
    
  else:
    project_form = ProjectForm()
  
  return render(request, 'registration/profile.html', { 'projects': projects, 'project_form': project_form, 'error_message': error_message })

@login_required
def project_delete(request, project_id):
	Project.objects.get(id=project_id).delete()
	return redirect('profile')

@login_required
def project_update(request, project_id):
  project = Project.objects.get(id=project_id)
  
  if request.method == 'POST':
    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid():
      project_to_update = form.save()
      if project_to_update.current == True :
        profile = Profile.objects.get(user=request.user)
        profile.current_project = project_to_update
        profile.save()
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

@login_required
def post_update(request, post_id, destination):
  post = Post.objects.get(id=post_id)
  
  if request.method == 'POST':
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
      post_to_update = form.save()
    return redirect('destination')
      
  else:
    form = ProjectForm(instance=project)
    
  return render(request, 'registration/profile.html', {'form': form})

