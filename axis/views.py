from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm


from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Define the home view
def home(request):
      return render(request, 'homepage.html')

def geography(request):
    return render(request, 'geography.html')

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


# def project_delete(request, trip_id):
# 	Trip.objects.get(id=trip_id).delete()
# 	return redirect('trips')


# def project_update(request, trip_id):
# 	trip = Trip.objects.get(id=trip_id)

# 	if request.method == 'POST':
# 		form = TripForm(request.POST, instance=trip)
# 		if form.is_valid():
# 			new_Trip = form.save()
# 			return redirect('trip_details', trip.id)
# 	else:
# 		form = TripForm(instance=trip)
# 	return render(request, 'trip_update.html', {'form': form})
