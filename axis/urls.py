from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('geography/', views.geography, name='geography'),
    path('accounts/signup', views.signup, name='signup'),
]