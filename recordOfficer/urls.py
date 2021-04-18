from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     # path('record-officer/', views.record_officer_view, name="record-officer"),
     path('', views.roHomeView,name="record-officer-home"),

     path('insert-letters-in/', views.insert_letters_in, name="insert-letters-in"),     
     path('insert-memo-in/', views.insert_memo_in, name="insert-memo-in"),
     path('insert-memo-out/', views.insert_memo_out, name="insert-memo-out"),
     path('view-memo-list/', views.view_memo_list, name="view-memo-list"),
     path('view-memo-out/', views.view_memo_out, name="view-memo-out"),
     path('view-letter-list/', views.view_letter_list, name="view-letter-list"),
     path('view-letter-out/', views.view_letter_out, name="view-letter-out"),
     path('insert-letters-out/', views.insert_letters_out, name="insert-letters-out"),
     # path('director/', views.director_view, name="director"),
     # path('human-resources/', views.hr_view, name="hr"),
     # path('human-resources/register-employees', views.register_employees, name="register-employees"),
          # path('incomingletters/<id>/', letter_in_detail, name='letter-detail-1'),
     path('incomingletters/<id>/update', views.incomingLettersUpdate , name='letter-update-1'),
     path('incomingletters/<id>/delete', views.incomingLettersDelete , name='letter-delete-1'),
     path('outgoingletters/<id>/update', views.outgoingLettersUpdate , name='letter-update-2'),
     path('outgoingletters/<id>/delete', views.outgoingLettersDelete , name='letter-delete-2'),
     path('incomingmemos/<id>/update', views.incomingMemosUpdate , name='memo-update-1'),
     path('incomingmemos/<id>/delete', views.incomingMemosDelete , name='memo-delete-1'),
     path('outgoingmemos/<id>/update', views.outgoingMemosUpdate , name='memo-update-2'),
     path('outgoingmemos/<id>/delete', views.outgoingMemosDelete , name='memo-delete-2'),
     path('user/<id>/update', views.userProfileUpdate , name='ro-update'),
     path('user/<id>/', views.detailProfile , name='ro-profile'),


]
