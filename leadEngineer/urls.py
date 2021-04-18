from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
     path('', views.leadEngineerHomeView, name="lead-engineer-home"),
     path('user/<id>/update', views.userProfileUpdate , name='le-update'),
     path('user/<id>/', views.detailProfile , name='le-profile'),
     path('incoming-letters/', views.leadEngineerIncomingLetter,name="le-incoming-letter"),
     path('incoming-memos/', views.leadEngineerIncomingMemo,name="le-incoming-memo"),
     path('outgoing-memos/', views.leadEngineerOutgoingMemo,name="le-outgoing-memo"),
     path('projects/', views.view_projects_list , name='le-projects'),
     path('outgoing-letters/', views.leadEngineerOutgoingLetter,name="le-outgoing-letter"),
     path('projects/<id>/details', views.projectDetails , name='le-projects-details'),
     path('projects/<id>/update', views.projectsUpdate , name='le-projects-update'),
     path('incoming-letters/<id>/forward', views.incomingLettersForward,name="le-incoming-letter-forward"),
     path('outgoing-letters/<id>/forward', views.outgoingLettersForward,name="le-outgoing-letter-forward"),
     path('incoming-memos/<id>/forward', views.incomingMemosForward,name="le-incoming-memo-forward"),
     path('outgoing-memos/<id>/forward', views.outgoingMemosForward,name="le-outgoing-memo-forward"),







]
