from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('geography/', views.geography, name='geography'),
]