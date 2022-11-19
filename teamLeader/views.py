from authentication.models import User
from bootstrap_datepicker_plus import DatePickerInput
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.shortcuts import (HttpResponseRedirect, get_list_or_404,
                              get_object_or_404, redirect, render)
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView
from humanResources.forms import profileUpdateForm
from recordOfficer.models import *

from teamLeader.forms import *
from .models import *

tl_login_required = user_passes_test(
    lambda user: True if user.title == 'Team Leader' and not user.is_admin else False, login_url='/')


def only_tl(view_func):
    decorated_view_func = login_required(
        tl_login_required(view_func), login_url='/')
    return decorated_view_func



@only_tl
def teamLeaderHomeView(request):
    return render(request, 'teamLeader/index.html')



@only_tl
def userProfileUpdate(request, id):
    obj = get_object_or_404(User, id=id)
    dire = User.objects.filter(username=request.user)
    if obj in dire:
        form = profileUpdateForm(request.POST or None,
                                 request.FILES or None, instance=obj)
        if form.is_valid():
            ref = form.cleaned_data["username"]
            form.save()
            messages.success(
                request, f'"{ ref }"   your profile has been updated!')
            url = request.get_full_path()
            this = url.replace('update', '')
            return redirect(this)

        context = {
            'form': form,
            'name': obj,
        }
        return render(request, "teamLeader/update_view.html", context)
    else:
        messages.warning(
            request, f'You have no authorization to access or edit other users profiles!')
        return redirect('team-leader-home')


@only_tl
def detailProfile(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
    # add the dictionary during initialization
    try:
        context["data"] = User.objects.get(id = id)
    except:
        print("None")
    if int(id) != request.user.id:
        messages.warning(request,f'You have no authorization to access or edit other users profiles!')
        return redirect('team-leader-home')
    else:
        return render(request, "teamLeader/profile.html", context)




@only_tl
def teamLeaderIncomingLetter(request):
    lists = IncomingLetters.objects.filter(directorate=request.user.directorate, level__gt = 1 ).order_by('byTeamleader')
    projects = Projects.objects.filter(directorate=request.user.directorate)
    context = {
        'lists' : lists,
        'projects' : projects,
    }

    return render(request, 'teamLeader/incoming_letters.html', context)




@only_tl
def teamLeaderIncomingMemo(request):
    lists = IncomingMemos.objects.filter(
        directorate=request.user.directorate, level__gt = 1).order_by('byTeamleader')
    return render(request, 'teamLeader/incoming_memos.html', {'lists': lists})

@only_tl
def teamLeaderOutgoingMemo(request):
    lists = OutgoingMemos.objects.filter(
        directorate=request.user.directorate, level__gt = 1).order_by('byTeamleader')
    return render(request, 'teamLeader/outgoing_memos.html', {'lists': lists})

@only_tl
def teamLeaderOutgoingLetter(request):
    lists = OutgoingLetters.objects.filter(directorate=request.user.directorate, level__gt = 1 ).order_by('byTeamleader')
    projects = Projects.objects.filter(directorate=request.user.directorate)
    context = {
        'lists' : lists,
        'projects' : projects,
    }
    return render(request, 'teamLeader/outgoing_letters.html', context)

@only_tl
def view_projects_list(request):
    projects = Projects.objects.filter(directorate=request.user.directorate, assignedTo=request.user.team).order_by('-dateAdded')
    return render(request, "teamLeader/projects.html", { 'projects' : projects})


# @only_tl
# def projectDetails(request,id):
#     projects = Projects.objects.filter(id=id, directorate=request.user.directorate, assignedTo=request.user.team)
#     return render(request, "teamLeader/project_details.html", { 'projects' : projects}) 

@only_tl
def projectDetails(request, id):
    obj = get_object_or_404(Projects, id = id)
    dire = Projects.objects.filter(id=id, directorate=request.user.directorate, assignedTo=request.user.team)
    
    if obj in dire:
        lead_engineer_id = obj.assignedToLE
        le = User.objects.filter(id=lead_engineer_id)
        form = projectDetailsForm(request.POST or None,
                                 request.FILES or None, instance = obj, lead_engineer_id = obj.assignedToLE )
        context = {
            'form': form,
            'name' : obj,
        }
        return render(request, "teamLeader/project_detail.html", context)
    else:
        messages.warning(
            request, f'You have no authorization to access or edit other directorates projects!')
        return redirect ('tl-projects')

# @only_tl
# def incomingLettersForward(request, id):
#     obj = get_object_or_404(IncomingLetters, id = id)
#     dire = IncomingLetters.objects.filter(directorate = request.user.directorate, level = '2' )
#     if obj in dire:
#         project = Projects.objects.get( id=obj.project.pk, directorate = request.user.directorate)
#         try:
#             teamLeader = User.objects.get(directorate = request.user.directorate, title='Lead Engineer', team=project.assignedTo)
#         except:
#             messages.warning(request, f"You cannot forward this letter! There is no Team Leader for this Project's assigned team.")
#             return redirect ('director-incoming-letter')

#         if request.method == 'POST':
#             form = forwardMessage(request.POST,firstName = teamLeader.firstName, middleName = teamLeader.middleName,instance = obj )
#             form2 = incomingLettersForm(instance = obj)
#             if form.is_valid():
#                 letter = form.save(commit=False)
#                 letter.author = request.user
#                 letter.save()
#                 forward = form2.save(commit=False)
#                 forward.byDirector = 'yes'
#                 forward.level = 2
#                 forward.save()
#                 messages.success(request, f'New Letter has been forwarded to team ( {project.assignedTo} ) --> {teamLeader.firstName} {teamLeader.middleName} !')
#                 return redirect('director-incoming-letter')
#         else:
#             form2 = incomingLettersForm(instance = obj)
#             form = forwardMessage(instance = obj, firstName = teamLeader.firstName, middleName = teamLeader.middleName)
#         try:
#             forwardList = DirectorsLetterMessages.objects.filter(referenceNumber = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")
#             context = {
#                 'name' : obj,
#                 'form2' : form2,
#                 'form' : form,
#                 'forwardList' : forwardList,
#             }
#         except:
#             context = {
#                 'name' : obj,
#                 'form2' : form2,
#                 'form' : form,
#             }


#         # forward = form2.save(commit=False)
#         # forward.byDirector = 'yes'
#         # forward.save()
#         return render(request, "director/forward.html", context)
#     else:
#         return redirect ('director-incoming-letter')    


@only_tl
def projectsUpdate(request, id):
    obj = get_object_or_404(Projects, id = id)
    dire = Projects.objects.filter(directorate = request.user.directorate, assignedTo = request.user.team )
    if obj in dire:
        form = editProjects(request.POST or None,
                                 request.FILES or None, instance = obj,director=request.user.directorate,team=request.user.team)
        if form.is_valid():
            form.save()
            messages.success(request, f'This Project has been forwarded and updated!')
            return redirect('tl-projects')

        context = {
            'form': form,
            'name' : obj,
        }
        return render(request, "teamLeader/update_view.html", context)
    else:
        messages.warning(
            request, f'You have no authorization to access or edit other directorates projects!')
        return redirect ('tl-projects')



@only_tl
def incomingLettersForward(request, id):
    obj = get_object_or_404(IncomingLetters, id = id)
    dire = IncomingLetters.objects.filter(directorate = request.user.directorate)
    if obj in dire:
        project = Projects.objects.get( id=obj.project.pk, directorate = request.user.directorate, assignedTo = request.user.team)
        try:
            leadEngineer = User.objects.get(directorate = request.user.directorate, title='Lead Engineer', team=project.assignedTo)
        except:
            messages.warning(request, f"You cannot forward this letter! There is no Lead Engineer assigned to for this Project.")
            return redirect ('tl-incoming-letter')

        if request.method == 'POST':
            form = forwardMessage(request.POST,firstName = leadEngineer.firstName, middleName = leadEngineer.middleName,instance = obj )
            form2 = incomingLettersForm(instance = obj)
            if form.is_valid():
                letter = form.save(commit=False)
                letter.author = request.user
                letter.save()
                forward = form2.save(commit=False)
                forward.byTeamleader = 'yes'
                forward.level = 3
                forward.save()
                messages.success(request, f'New Letter has been forwarded to team ( {project.assignedTo} ) --> {leadEngineer.firstName} {leadEngineer.middleName} !')
                return redirect('tl-incoming-letter')
        else:
            form = forwardMessage(instance = obj, firstName = leadEngineer.firstName, middleName = leadEngineer.middleName)
        tlforwardList = TeamLeadersLetterMessages.objects.filter(referenceNumber = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")
        print('ssssssssssssssssssssssssssssssssssssssssssssssssssssssssss')
        print(tlforwardList)   
        try:
            forwardList = DirectorsLetterMessages.objects.filter(referenceNumber = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")
            tlforwardList = TeamLeadersLetterMessages.objects.filter(referenceNumber = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")
            print('sssssssssssssssssssssssssssssssssssss')
            print(tlforwardList)
            context = {
                'name' : obj,
                'form' : form,
                'forwardList' : forwardList,
                'tlforwardList' : tlforwardList,
            }
        except:

            context = {
                'name' : obj,
                'form' : form,
                'forwardList' : forwardList,

            }


        # forward = form2.save(commit=False)
        # forward.byDirector = 'yes'
        # forward.save()
        return render(request, "teamLeader/forward.html", context)
    else:
        return redirect ('tl-incoming-letter')    



@only_tl
def outgoingLettersForward(request, id):
    obj = get_object_or_404(OutgoingLetters, id = id)
    dire = OutgoingLetters.objects.filter(directorate = request.user.directorate)
    if obj in dire:
        project = Projects.objects.get( id=obj.project.pk, directorate = request.user.directorate, assignedTo = request.user.team)
        try:
            leadEngineer = User.objects.get(directorate = request.user.directorate, title='Lead Engineer', team=project.assignedTo)
        except:
            messages.warning(request, f"You cannot forward this letter! There is no Lead Engineer assigned to for this Project.")
            return redirect ('tl-outgoing-letter')

        if request.method == 'POST':
            form = forwardOutLetter(request.POST,firstName = leadEngineer.firstName, middleName = leadEngineer.middleName,instance = obj )
            form2 = outgoingLettersForm(instance = obj)
            if form.is_valid():
                letter = form.save(commit=False)
                letter.author = request.user
                letter.save()
                forward = form2.save(commit=False)
                forward.byTeamleader = 'yes'
                forward.level = 3
                forward.save()
                messages.success(request, f'New Letter has been forwarded to team ( {project.assignedTo} ) --> {leadEngineer.firstName} {leadEngineer.middleName} !')
                return redirect('tl-outgoing-letter')
        else:
            form = forwardOutLetter(instance = obj, firstName = leadEngineer.firstName, middleName = leadEngineer.middleName)
        tlforwardList = TeamLeadersLetterMessagesOut.objects.filter(referenceNumber = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")
        print('ssssssssssssssssssssssssssssssssssssssssssssssssssssssssss')
        print(tlforwardList)   
        try:
            forwardList = DirectorsLetterMessagesOut.objects.filter(referenceNumber = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")
            tlforwardList = TeamLeadersLetterMessagesOut.objects.filter(referenceNumber = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")
            print('sssssssssssssssssssssssssssssssssssss')
            print(tlforwardList)
            context = {
                'name' : obj,
                'form' : form,
                'forwardList' : forwardList,
                'tlforwardList' : tlforwardList,
            }
        except:

            context = {
                'name' : obj,
                'form' : form,
                'forwardList' : forwardList,

            }
        # forward = form2.save(commit=False)
        # forward.byDirector = 'yes'
        # forward.save()
        return render(request, "teamLeader/forward.html", context)
    else:
        return redirect ('tl-outgoing-letter')    



@only_tl
def incomingMemosForward(request, id):
    obj = get_object_or_404(IncomingMemos, id = id)
    dire = IncomingMemos.objects.filter(directorate = request.user.directorate)
    if obj in dire:
        project = Projects.objects.get( id=obj.project.pk, directorate = request.user.directorate, assignedTo = request.user.team, assignedToLE = request.user.id)
        try:
            leadEngineer = User.objects.get(directorate = request.user.directorate, title='Lead Engineer', team=project.assignedTo)
        except:
            messages.warning(request, f"You cannot forward this Memo! There is no Lead Engineer assigned to for this Project.")
            return redirect ('tl-incoming-memo')

        if request.method == 'POST':
            form = forwardInMemo(request.POST,firstName = leadEngineer.firstName, middleName = leadEngineer.middleName,instance = obj )
            form2 = incomingMemosForm(instance = obj)
            if form.is_valid():
                letter = form.save(commit=False)
                letter.author = request.user
                letter.save()
                forward = form2.save(commit=False)
                forward.byTeamleader = 'yes'
                forward.level = 3
                forward.save()
                messages.success(request, f'New Memo has been forwarded to team ( {project.assignedTo} ) --> {leadEngineer.firstName} {leadEngineer.middleName} !')
                return redirect('tl-incoming-memo')
        else:
            form2 = incomingMemosForm(instance = obj)
            form = forwardInMemo(instance = obj, firstName = leadEngineer.firstName, middleName = leadEngineer.middleName)
        try:
            forwardList = DirectorsMemoMessages.objects.filter(subject = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")
            tlforwardList = TeamLeadersMemoMessages.objects.filter(subject = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")
            context = {
                'name' : obj,
                'form2' : form2,
                'form' : form,
                'forwardList' : forwardList,
                'tlforwardList' : tlforwardList,

            }
        except:
            context = {
                'name' : obj,
                'form2' : form2,
                'form' : form,
                'forwardList' : forwardList,

            }


        # forward = form2.save(commit=False)
        # forward.byDirector = 'yes'
        # forward.save()
        return render(request, "teamLeader/forward.html", context)
    else:
        return redirect ('tl-incoming-memo')    



@only_tl
def outgoingMemosForward(request, id):
    obj = get_object_or_404(OutgoingMemos, id = id)
    dire = OutgoingMemos.objects.filter(directorate = request.user.directorate)
    if obj in dire:
        project = Projects.objects.get( id=obj.project.pk, directorate = request.user.directorate,assignedTo = request.user.team, assignedToLE = request.user.id)
        try:
            leadEngineer = User.objects.get(directorate = request.user.directorate, title='Lead Engineer', team=project.assignedTo)
        except:
            messages.warning(request, f"You cannot forward this Memo! There is no Lead Engineer assigned to for this Project.")
            return redirect ('tl-outgoing-memo')

        if request.method == 'POST':
            form = forwardOutMemo(request.POST,firstName = leadEngineer.firstName, middleName = leadEngineer.middleName,instance = obj )
            form2 = outgoingMemosForm(instance = obj)
            if form.is_valid():
                letter = form.save(commit=False)
                letter.author = request.user
                letter.save()
                forward = form2.save(commit=False)
                forward.byTeamleader = 'yes'
                forward.level = 3
                forward.save()
                messages.success(request, f'New Memo has been forwarded to team ( {project.assignedTo} ) --> {leadEngineer.firstName} {leadEngineer.middleName} !')
                return redirect('tl-outgoing-memo')
        else:
            form2 = outgoingMemosForm(instance = obj)
            form = forwardOutMemo(instance = obj, firstName = leadEngineer.firstName, middleName = leadEngineer.middleName)
        try:
            forwardList = DirectorsMemoMessagesOut.objects.filter(subject = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")
            tlforwardList = TeamLeadersMemoMessagesOut.objects.filter(subject = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")
            context = {
                'name' : obj,
                'form2' : form2,
                'form' : form,
                'forwardList' : forwardList,
                'tlforwardList' : tlforwardList,

            }
        except:
            context = {
                'name' : obj,
                'form2' : form2,
                'form' : form,
                'forwardList' : forwardList,

            }


        # forward = form2.save(commit=False)
        # forward.byDirector = 'yes'
        # forward.save()
        return render(request, "teamLeader/forward.html", context)
    else:
        return redirect ('tl-outgoing-memo')   