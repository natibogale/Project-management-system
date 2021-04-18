from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
     path('', views.projectEngineerHomeView, name="project-engineer-home"),
     path('user/<id>/update', views.userProfileUpdate , name='pe-update'),
     path('user/<id>/', views.detailProfile , name='pe-profile'),
     path('incoming-letters/', views.projectEngineerIncomingLetter,name="pe-incoming-letter"),
     path('incoming-memos/', views.projectEngineerIncomingMemo,name="pe-incoming-memo"),
     path('outgoing-memos/', views.projectEngineerOutgoingMemo,name="pe-outgoing-memo"),
     path('projects/', views.view_projects_list , name='pe-projects'),
     path('outgoing-letters/', views.projectEngineerOutgoingLetter,name="pe-outgoing-letter"),
     path('projects/<id>/details', views.projectDetails , name='pe-projects-details'),
     # path('projects/<id>/update', views.projectsUpdate , name='pe-projects-update'),
     path('incoming-letters/<id>/messages', views.incomingLettersForward,name="pe-incoming-letter-forward"),
     path('outgoing-letters/<id>/messages', views.outgoingLettersForward,name="pe-outgoing-letter-forward"),
     path('incoming-memos/<id>/messages', views.incomingMemosForward,name="pe-incoming-memo-forward"),
     path('outgoing-memos/<id>/messages', views.outgoingMemosForward,name="pe-outgoing-memo-forward"),







]
