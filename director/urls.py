from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    #  path('record-officer/', views.record_officer_view, name="record-officer"),
    #  path('director/', views.director_view, name="director"),
    #  path('human-resources/', views.hr_view, name="hr"),
     path('', views.directorHomeView,name="director-home"),
     path('incoming-letters/', views.directorIncomingLetter,name="director-incoming-letter"),
     path('incoming-memos/', views.directorIncomingMemo,name="director-incoming-memo"),
     path('outgoing-memos/', views.directorOutgoingMemo,name="director-outgoing-memo"),
     path('outgoing-letters/', views.directorOutgoingLetter,name="director-outgoing-letter"),
     path('user/<id>/update', views.userProfileUpdate , name='dr-update'),
     path('user/<id>/', views.detailProfile , name='dr-profile'),
     path('projects/', views.view_projects_list , name='dr-projects'),
     path('add-projects/', views.addProjects , name='dr-add-projects'),
     path('projects/<id>/update', views.projectsUpdate , name='dr-projects-update'),
     path('projects/<id>/details', views.projectDetails , name='dr-projects-details'),
     path('projects/<id>/delete', views.projectsDelete , name='dr-projects-delete'),
     path('incoming-letters/<id>/forward', views.incomingLettersForward,name="dr-incoming-letter-forward"),
     path('outgoing-letters/<id>/forward', views.outgoingLettersForward,name="dr-outgoing-letter-forward"),
     path('incoming-memos/<id>/forward', views.incomingMemosForward,name="dr-incoming-memo-forward"),
     path('outgoing-memos/<id>/forward', views.outgoingMemosForward,name="dr-outgoing-memo-forward"),







]
