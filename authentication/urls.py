from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
     path('record-officer/', include('recordOfficer.urls')),
     path('director/', include('director.urls')),
     path('human-resources/', include('humanResources.urls')),
     path('team-leader/', include('teamLeader.urls')),
     path('lead-engineer/', include('leadEngineer.urls')),
     path('project-engineer/', include('projectEngineer.urls')),
     path('', views.home,name="home"),
]
