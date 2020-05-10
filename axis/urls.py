from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('resources/', views.resources, name='resources'),
    #project management
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/profile', views.profile, name='profile'),
    path('project/<int:project_id>/delete', views.project_delete, name='project_delete'),
    path('accounts/project/<int:project_id>/update', views.project_update, name='project_update'),
    #posts and pictures
    path('<slug:domain>/post/<int:post_id>/delete', views.post_delete, name='post_delete'),
    path('<slug:domain>/post/<int:post_id>/update', views.post_update, name='post_update'),
    path('picture/<int:picture_id>/delete', views.picture_delete, name='picture_delete'),
    # domains
    path('<slug:project_name>/geography/', views.geography, name='geography'),
    path('<slug:project_name>/culture/', views.culture, name='culture'),
    path('<slug:project_name>/government/', views.government, name='government'),
    path('<slug:project_name>/history/', views.history, name='history'),
    path('<slug:project_name>/religion/', views.religion, name='religion'),
    path('<slug:project_name>/warfare/', views.warfare, name='warfare'),
]