from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from .views import employeesUpdate


urlpatterns = [
     path('register-employees', views.registrationView, name="register-employees"),
     path('', views.hrHomeView, name="human-resources-home"),
     path('employees-list/',views.employeesList, name="hr-employees-list"),
     path('update-employees/<pk>/update', employeesUpdate.as_view(), name='update-employees'),
     path('user/<id>/update', views.userProfileUpdate , name='hr-update'),
     path('user/<id>/', views.detailProfile , name='hr-profile'),


]
