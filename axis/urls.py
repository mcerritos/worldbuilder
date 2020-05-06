from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #project management
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/profile', views.profile, name='profile'),
    path('project/<int:project_id>/delete', views.project_delete, name='project_delete'),
    path('accounts/project/<int:project_id>/update', views.project_update, name='project_update'),
    #posts
    path('post/<int:post_id>/delete', views.post_delete, name='post_delete'),
    path('post/<int:post_id>/update', views.post_update, name='post_update'),
    # domains
    path('geography/', views.geography, name='geography'),
    path('culture/', views.culture, name='culture'),
    path('government/', views.government, name='government'),
    path('history/', views.history, name='history'),
    path('religion/', views.religion, name='religion'),
    path('warfare/', views.warfare, name='warfare'),
]