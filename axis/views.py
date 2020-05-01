from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Define the home view
def home(request):
      return render(request, 'homepage.html')

def geography(request):
    return render(request, 'geography.html')