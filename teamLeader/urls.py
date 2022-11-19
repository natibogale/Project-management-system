from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
     path('', views.teamLeaderHomeView, name="team-leader-home"),
     # path('employees-list/',views.employeesList, name="hr-employees-list"),
     path('user/<id>/update', views.userProfileUpdate , name='tl-update'),
     path('user/<id>/', views.detailProfile , name='tl-profile'),
     path('incoming-letters/', views.teamLeaderIncomingLetter,name="tl-incoming-letter"),
     path('incoming-memos/', views.teamLeaderIncomingMemo,name="tl-incoming-memo"),
     path('outgoing-memos/', views.teamLeaderOutgoingMemo,name="tl-outgoing-memo"),
     path('projects/', views.view_projects_list , name='tl-projects'),
     path('outgoing-letters/', views.teamLeaderOutgoingLetter,name="tl-outgoing-letter"),
     path('projects/<id>/details', views.projectDetails , name='tl-projects-details'),
     path('projects/<id>/update', views.projectsUpdate , name='tl-projects-update'),
     path('incoming-letters/<id>/forward', views.incomingLettersForward,name="tl-incoming-letter-forward"),
     path('outgoing-letters/<id>/forward', views.outgoingLettersForward,name="tl-outgoing-letter-forward"),
     path('incoming-memos/<id>/forward', views.incomingMemosForward,name="tl-incoming-memo-forward"),
     path('outgoing-memos/<id>/forward', views.outgoingMemosForward,name="tl-outgoing-memo-forward"),







]
