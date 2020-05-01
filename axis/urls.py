from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('geography/', views.geography, name='geography'),
    path('accounts/signup', views.signup, name='signup'),
    #project management
    path('accounts/profile', views.profile, name='profile'),
    # path('profile/<int:project_id>/', views.project_details, name='project_details'),
    path('project/<int:project_id>/delete', views.project_delete, name='project_delete'),
    path('project/<int:project_id>/update', views.project_update, name='project_update'),
    
]