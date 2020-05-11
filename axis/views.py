from django.shortcuts import render, redirect
from .models import Project, Profile, Post, Picture, Warfare, Culture, Government, Religion, Question, Geography, History
from .forms import ProjectForm, PostForm, PictureForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

placeholder = Project.objects.get(name="Anonymous")

def getCurrentProject(request, project_name):
  try: 
    profile = Profile.objects.get(user=request.user)
    project_id = profile.current_project
    print("This is the try block.")
  except:
    project_id= placeholder
    print("This is the except block.")
  return project_id

def home(request):
  project_id = getCurrentProject(request, "placeholder")
  return render(request, 'homepage.html', {'current_project': project_id} )

def about(request):
  project_id = getCurrentProject(request, "placeholder")
  return render(request, 'about.html', {'current_project': project_id})

def resources(request):
  project_id = getCurrentProject(request, "placeholder")
  return render(request, 'resources.html', {'current_project': project_id})
### functions to handle functionality that is the same across different routes

domains = [Culture, Warfare, Government, Religion, Geography, History]

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

def handlePicture (request, data, d_name):
    form = PictureForm(data, request.FILES)
    if form.is_valid():
        form.save() 
        print(form)
        redirect("domains/"+d_name+"/") 


def createNewProject(project_form, request, populated):
  if populated:
    new_project = project_form.save()
  else:
    try:
      new_project = Project.objects.create(name=request.user.username, current=True)
    except:
      number = Project.objects.filter(users=request.user).count()
      number += 1
      project_name = "Project " + str(number)
      new_project = Project.objects.create(name=project_name, current=True)
  
  new_project.users.add(request.user)
  new_project.save()
  
  # create domains when project made
  for dom in domains:
    new_domain = dom.objects.create(project=new_project)
    domain_questions = Question.objects.filter(domain=dom)
    starting_summary = Post.objects.create(title="Summary", author=request.user, text="This is your domain summary. You can fill it out with whatever you like. You can place a broad overview of the topics that you want to address, or talk about statistics, characters, campaigns, or anything else you want to immediately link with the domain. The choice is yours!", position="Sum")
    new_domain.posts.add(starting_summary)
    for q in domain_questions:
      new_domain.questions.add(q)
      new_domain.save()

  #get profile associated with user and set current project to the new project
  profile = Profile.objects.get(user=request.user)
  profile.current_project = new_project
  profile.save()
    
  return redirect('profile')

################################# domain pages
def culture(request, project_name):
  project_id = getCurrentProject(request, project_name)
  c = Culture.objects.get(project=project_id)
  questions = Question.objects.filter(culture=c).all()
  summaries = Post.objects.filter(culture=c).filter(position="Sum")
  posts = Post.objects.filter(culture=c).filter(position="Ssc")

  if request.method == 'POST' and request.FILES:
    data = {'user':request.user,'project': project_id, 'domain': "Culture"}
    handlePicture(request, data, "Culture")

  if request.method == 'POST':
    handlePost(request, c, "culture")
  
  post_form = PostForm()
  pictures= Picture.objects.filter(project=project_id).filter(domain="Culture")
  context = {'questions' : questions, 'posts': posts,
  'summaries': summaries, 'post_form': post_form, 'current_project': project_id, 'domain': "culture"}
  return render(request, 'domains/culture.html', context )

def government(request, project_name):
  project_id = getCurrentProject(request, project_name)
  gov = Government.objects.get(project=project_id)
  questions = Question.objects.filter(government=gov).all()
  summaries = Post.objects.filter(government=gov).filter(position="Sum")
  posts = Post.objects.filter(government=gov).filter(position="Ssc")

  if request.method == 'POST' and request.FILES:
    data = {'user':request.user,'project': project_id, 'domain': "Government"}
    handlePicture(request, data, "Government")

  if request.method == 'POST':
    handlePost(request, gov, "government")
    
  post_form = PostForm()
  pictures= Picture.objects.filter(project=project_id).filter(domain="Government")
  context = {'questions' : questions, 'posts': posts, 'summaries': summaries, 'post_form': post_form, 'current_project': project_id, 'domain': "government"}
  return render(request, 'domains/government.html', context)

def history(request, project_name):
  project_id = getCurrentProject(request, project_name)
  hist = History.objects.get(project=project_id)
  questions = Question.objects.filter(history=hist).all()
  summaries = Post.objects.filter(history=hist).filter(position="Sum")
  posts = Post.objects.filter(history=hist).filter(position="Ssc")

  if request.method == 'POST' and request.FILES:
    data = {'user':request.user,'project': project_id, 'domain': "History"}
    handlePicture(request, data, "History")

  if request.method == 'POST':
    handlePost(request, hist, "History")
    
  post_form = PostForm()
  pictures= Picture.objects.filter(project=project_id).filter(domain="History")
  context = {'questions' : questions, 'posts': posts, 'summaries': summaries, 'post_form': post_form, 'current_project': project_id, 'domain': "history"}
  return render(request, 'domains/history.html', context)

def religion(request, project_name):
  project_id = getCurrentProject(request, project_name)
  r = Religion.objects.get(project=project_id)
  questions = Question.objects.filter(religion=r).all()
  summaries = Post.objects.filter(religion=r).filter(position="Sum")
  posts = Post.objects.filter(religion=r).filter(position="Ssc")

  if request.method == 'POST' and request.FILES:
    data = {'user':request.user,'project': project_id, 'domain': "Religion"}
    handlePicture(request, data, "Religion")

  if request.method == 'POST':
    handlePost(request, r, "religion")
  
  post_form = PostForm()
  pictures= Picture.objects.filter(project=project_id).filter(domain="Religion")
  context = {'questions' : questions, 'posts': posts,'summaries': summaries, 'post_form': post_form, 'current_project': project_id, 'domain': "religion"}
  return render(request, 'domains/religion.html', context )

def geography(request, project_name):
  project_id = getCurrentProject(request, project_name)
  geo = Geography.objects.get(project=project_id)
  questions = Question.objects.filter(geography=geo).all()
  summaries = Post.objects.filter(geography=geo).filter(position="Sum")
  posts = Post.objects.filter(geography=geo).filter(position="Ssc")

  if request.method == 'POST' and request.FILES:
    data = {'user':request.user,'project': project_id, 'domain': "Geography"}
    handlePicture(request, data, "Geography")

  elif request.method == 'POST':
    handlePost(request, geo, "geography")
    
  post_form = PostForm()
  picture_form = PictureForm(initial={'user':request.user,'project': project_id})
  pictures= Picture.objects.filter(project=project_id).filter(domain="Geography")
  context = {'questions' : questions, 'posts': posts, 'summaries': summaries, 'post_form': post_form, 'current_project': project_id, 'picture_form': picture_form, 'pictures': pictures, 'domain': "geography"}
  return render(request, 'domains/geography.html', context)

def warfare(request, project_name):
  project_id = getCurrentProject(request, project_name)
  w = Warfare.objects.get(project=project_id)
  questions = Question.objects.filter(warfare=w).all()
  summaries = Post.objects.filter(warfare=w).filter(position="Sum")
  posts = Post.objects.filter(warfare=w).filter(position="Ssc")

  if request.method == 'POST' and request.FILES:
    data = {'user':request.user,'project': project_id, 'domain': "Warfare"}
    handlePicture(request, data, "Warfare")

  if request.method == 'POST':
    handlePost(request, w, "warfare")
  
  post_form = PostForm()
  pictures= Picture.objects.filter(project=project_id).filter(domain="Warfare")
  context = {'questions' : questions, 'posts': posts, 'summaries': summaries, 'post_form': post_form, 'current_project': project_id, 'domain': "warfare"}
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
      return redirect('profile')
    else:
      error_message = 'Invalid sign up - try again'

  form = UserCreationForm()
  project_id = getCurrentProject(request, "anonymous")
  context = {'form': form, 'error_message': error_message, 'current_project': project_id}
  return render(request, 'registration/signup.html', context)

#################################### project crud + profile
@login_required
def profile(request):
  error_message = ''
  project_id = getCurrentProject(request, "placeholder")
  projects = Project.objects.filter(users=request.user)
  pictures= Picture.objects.filter(project=project_id).filter(domain="Geography")
  
  # project creation if posted
  if request.method == 'POST':
    project_form = ProjectForm(request.POST)
    if project_form.is_valid() :
      createNewProject(project_form, request, True)
    else:
      error_message = 'Invalid project - try again'
    
  else:
    project_form = ProjectForm()

  context= { 'projects': projects, 'project_form': project_form, 'error_message': error_message, 'current_project': project_id, 'pictures':pictures };
  
  return render(request, 'registration/profile.html', context )

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
def post_delete(request, domain, post_id):
  project_id = getCurrentProject(request, "placeholder")
  ## post author is user.request
  this_post = Post.objects.get(id=post_id)
  if (this_post.author == request.user):
    Post.objects.get(id=post_id).delete()
  
  return redirect(domain, project_id)

@login_required
def post_update(request, domain, post_id):
  project_id = getCurrentProject(request, "placeholder")
  post = Post.objects.get(id=post_id)
  
  if request.method == 'POST' and post.position == 'Sum':
    form = PostForm(request.POST, instance=post)
    print(form)
  
  if request.method == 'POST':
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
      print("valid")
      post_to_update = form.save()
      return redirect(domain, project_id)
    else:
      print(form)
      
  else:
    form = ProjectForm(instance=project)
  
  return redirect(domain, project_id)

@login_required
def picture_delete(request, picture_id):
	Picture.objects.get(id=picture_id).delete()
	return redirect('profile')

