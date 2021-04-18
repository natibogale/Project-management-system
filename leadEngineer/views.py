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

from leadEngineer.forms import *
from .models import *

le_login_required = user_passes_test(
    lambda user: True if user.title == 'Lead Engineer' and not user.is_admin else False, login_url='/')


def only_le(view_func):
    decorated_view_func = login_required(
        le_login_required(view_func), login_url='/')
    return decorated_view_func




@only_le
def leadEngineerHomeView(request):
    return render(request, 'leadEngineer/index.html')    





@only_le
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
        return render(request, "leadEngineer/update_view.html", context)
    else:
        messages.warning(
            request, f'You have no authorization to access or edit other users profiles!')
        return redirect('lead-engineer-home')



@only_le
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
        return redirect('lead-engineer-home')
    else:
        return render(request, "leadEngineer/profile.html", context)


@only_le
def leadEngineerIncomingLetter(request):
    lists = IncomingLetters.objects.filter(directorate=request.user.directorate, level__gt = 2 ).order_by('byleadengineer')
    projects = Projects.objects.filter(directorate=request.user.directorate)
    context = {
        'lists' : lists,
        'projects' : projects,
    }

    return render(request, 'leadEngineer/incoming_letters.html', context)


@only_le
def leadEngineerIncomingMemo(request):
    lists = IncomingMemos.objects.filter(
        directorate=request.user.directorate, level__gt = 2).order_by('byleadengineer')
    return render(request, 'leadEngineer/incoming_memos.html', {'lists': lists})

@only_le
def leadEngineerOutgoingMemo(request):
    lists = OutgoingMemos.objects.filter(
        directorate=request.user.directorate, level__gt = 2).order_by('byleadengineer')
    return render(request, 'leadEngineer/outgoing_memos.html', {'lists': lists})

@only_le
def leadEngineerOutgoingLetter(request):
    lists = OutgoingLetters.objects.filter(directorate=request.user.directorate, level__gt = 2 ).order_by('byleadengineer')
    projects = Projects.objects.filter(directorate=request.user.directorate)
    context = {
        'lists' : lists,
        'projects' : projects,
    }
    return render(request, 'leadEngineer/outgoing_letters.html', context)




@only_le
def view_projects_list(request):
    projects = Projects.objects.filter(directorate=request.user.directorate, assignedTo=request.user.team, assignedToLE=request.user.id).order_by('-dateAdded')
    return render(request, "leadEngineer/projects.html", { 'projects' : projects})


@only_le
def projectDetails(request, id):
    obj = get_object_or_404(Projects, id = id)
    dire = Projects.objects.filter(id=id, directorate=request.user.directorate, assignedTo=request.user.team,assignedToLE=request.user.id)
    
    if obj in dire:
        lead_engineer_id = obj.assignedToLE
        le = User.objects.filter(id=lead_engineer_id)
        form = projectDetailsForm(request.POST or None,
                                 request.FILES or None, instance = obj, lead_engineer_id = obj.assignedToLE )
        context = {
            'form': form,
            'name' : obj,
        }
        return render(request, "leadEngineer/project_detail.html", context)
    else:
        messages.warning(
            request, f'You have no authorization to access or edit other directorates projects!')
        return redirect ('le-projects')


@only_le
def projectsUpdate(request, id):
    obj = get_object_or_404(Projects, id = id)
    dire = Projects.objects.filter(directorate = request.user.directorate, assignedTo = request.user.team,assignedToLE=request.user.id )
    if obj in dire:
        form = editProjects(request.POST or None,
                                 request.FILES or None, instance = obj,director=request.user.directorate,team=request.user.team)
        if form.is_valid():
            form.save()
            messages.success(request, f'This Project has been forwarded and updated!')
            return redirect('le-projects')

        context = {
            'form': form,
            'name' : obj,
        }
        return render(request, "leadEngineer/update_view.html", context)
    else:
        messages.warning(
            request, f'You have no authorization to access or edit other directorates projects!')
        return redirect ('le-projects')



@only_le
def incomingLettersForward(request, id):
    obj = get_object_or_404(IncomingLetters, id = id)
    dire = IncomingLetters.objects.filter(directorate = request.user.directorate)
    if obj in dire:
        project = Projects.objects.get( id=obj.project.pk, directorate = request.user.directorate, assignedTo = request.user.team, assignedToLE=request.user.id)
        try:
            projectEngineer = User.objects.get(directorate = request.user.directorate, title='Project Engineer', team=project.assignedTo)
        except:
            messages.warning(request, f"You cannot forward this letter! There is no Project Engineer assigned to for this Project.")
            return redirect ('le-incoming-letter')

        if request.method == 'POST':
            form = forwardMessage(request.POST,firstName = projectEngineer.firstName, middleName = projectEngineer.middleName,instance = obj )
            form2 = incomingLettersForm(instance = obj)
            if form.is_valid():
                letter = form.save(commit=False)
                letter.author = request.user
                letter.save()
                forward = form2.save(commit=False)
                forward.byleadengineer = 'yes'
                forward.level = 4
                forward.save()
                messages.success(request, f'New Letter has been forwarded to team ( {project.assignedTo} ) --> {projectEngineer.firstName} {projectEngineer.middleName} !')
                return redirect('le-incoming-letter',)
        else:
            form = forwardMessage(instance = obj, firstName = projectEngineer.firstName, middleName = projectEngineer.middleName) 
        try:
            forwardList = DirectorsLetterMessages.objects.filter(referenceNumber = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")
            tlforwardList = TeamLeadersLetterMessages.objects.filter(referenceNumber = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")
            leforwardList = LeadEngineersLetterMessages.objects.filter(referenceNumber = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")
            print('sssssssssssssssssssssssssssssssssssss')
            print(tlforwardList)
            context = {
                'name' : obj,
                'form' : form,
                'forwardList' : forwardList,
                'tlforwardList' : tlforwardList,
                'leforwardList' : leforwardList,
            }
        except:

            context = {
                'name' : obj,
                'form' : form,
                'forwardList' : forwardList,
                'tlforwardList': tlforwardList,

            }


        # forward = form2.save(commit=False)
        # forward.byDirector = 'yes'
        # forward.save()
        return render(request, "leadEngineer/forward.html", context)
    else:
        return redirect ('le-incoming-letter')  



@only_le
def outgoingLettersForward(request, id):
    obj = get_object_or_404(OutgoingLetters, id = id)
    dire = OutgoingLetters.objects.filter(directorate = request.user.directorate)
    if obj in dire:
        project = Projects.objects.get( id=obj.project.pk, directorate = request.user.directorate, assignedTo = request.user.team,assignedToLE=request.user.id)
        try:
            projectEngineer = User.objects.get(directorate = request.user.directorate, title='Project Engineer', team=project.assignedTo)
        except:
            messages.warning(request, f"You cannot forward this letter! There is no Project Engineer assigned to for this Project.")
            return redirect ('le-outgoing-letter')

        if request.method == 'POST':
            form = forwardOutLetter(request.POST,firstName = projectEngineer.firstName, middleName = projectEngineer.middleName,instance = obj )
            form2 = outgoingLettersForm(instance = obj)
            if form.is_valid():
                letter = form.save(commit=False)
                letter.author = request.user
                letter.save()
                forward = form2.save(commit=False)
                forward.byleadengineer = 'yes'
                forward.level = 4
                forward.save()
                messages.success(request, f'New Letter has been forwarded to team ( {project.assignedTo} ) --> {projectEngineer.firstName} {projectEngineer.middleName} !')
                return redirect('le-outgoing-letter')
        else:
            form = forwardOutLetter(instance = obj, firstName = projectEngineer.firstName, middleName = projectEngineer.middleName)
 
        try:
            forwardList = DirectorsLetterMessagesOut.objects.filter(referenceNumber = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")
            tlforwardList = TeamLeadersLetterMessagesOut.objects.filter(referenceNumber = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")
            leforwardList = LeadEngineersLetterMessagesOut.objects.filter(referenceNumber = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")
            print('sssssssssssssssssssssssssssssssssssss')
            print(tlforwardList)
            context = {
                'name' : obj,
                'form' : form,
                'forwardList' : forwardList,
                'tlforwardList' : tlforwardList,
                'leforwardList' : leforwardList,
            }
        except:

            context = {
                'name' : obj,
                'form' : form,
                'forwardList' : forwardList,
                'tlforwardList' : tlforwardList,

            }
        # forward = form2.save(commit=False)
        # forward.byDirector = 'yes'
        # forward.save()
        return render(request, "leadEngineer/forward.html", context)
    else:
        return redirect ('le-outgoing-letter')    




@only_le
def incomingMemosForward(request, id):
    obj = get_object_or_404(IncomingMemos, id = id)
    dire = IncomingMemos.objects.filter(directorate = request.user.directorate)
    if obj in dire:
        project = Projects.objects.get( id=obj.project.pk, directorate = request.user.directorate, assignedTo = request.user.team, assignedToLE = request.user.id)
        try:
            projectEngineer = User.objects.get(directorate = request.user.directorate, title='Project Engineer', team=project.assignedTo)
        except:
            messages.warning(request, f"You cannot forward this Memo! There is no Project Engineer assigned to for this Project.")
            return redirect ('le-incoming-memo')

        if request.method == 'POST':
            form = forwardInMemo(request.POST,firstName = projectEngineer.firstName, middleName = projectEngineer.middleName,instance = obj )
            form2 = incomingMemosForm(instance = obj)
            if form.is_valid():
                letter = form.save(commit=False)
                letter.author = request.user
                letter.save()
                forward = form2.save(commit=False)
                forward.byleadengineer = 'yes'
                forward.level = 4 
                forward.save()
                messages.success(request, f'New Memo has been forwarded to team ( {project.assignedTo} ) --> {projectEngineer.firstName} {projectEngineer.middleName} !')
                return redirect('le-incoming-memo')
        else:
            form2 = incomingMemosForm(instance = obj)
            form = forwardInMemo(instance = obj, firstName = projectEngineer.firstName, middleName = projectEngineer.middleName)
        try:
            forwardList = DirectorsMemoMessages.objects.filter(subject = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")
            tlforwardList = TeamLeadersMemoMessages.objects.filter(subject = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")
            leforwardList = LeadEngineersMemoMessages.objects.filter(subject = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")

            context = {
                'name' : obj,
                'form2' : form2,
                'form' : form,
                'forwardList' : forwardList,
                'tlforwardList' : tlforwardList,
                'leforwardList' : leforwardList,

            }
        except:
            context = {
                'name' : obj,
                'form2' : form2,
                'form' : form,
                'forwardList' : forwardList,
                'tlforwardList': tlforwardList

            }


        # forward = form2.save(commit=False)
        # forward.byDirector = 'yes'
        # forward.save()
        return render(request, "leadEngineer/forward.html", context)
    else:
        return redirect ('le-incoming-memo')    



@only_le
def outgoingMemosForward(request, id):
    obj = get_object_or_404(OutgoingMemos, id = id)
    dire = OutgoingMemos.objects.filter(directorate = request.user.directorate)
    if obj in dire:
        project = Projects.objects.get( id=obj.project.pk, directorate = request.user.directorate, assignedTo = request.user.team, assignedToLE = request.user.id)
        try:
            projectEngineer = User.objects.get(directorate = request.user.directorate, title='Project Engineer', team=project.assignedTo)
        except:
            messages.warning(request, f"You cannot forward this Memo! There is no Project Engineer assigned to for this Project.")
            return redirect ('tl-outgoing-memo')

        if request.method == 'POST':
            form = forwardOutMemo(request.POST,firstName = projectEngineer.firstName, middleName = projectEngineer.middleName,instance = obj )
            form2 = outgoingMemosForm(instance = obj)
            if form.is_valid():
                letter = form.save(commit=False)
                letter.author = request.user
                letter.save()
                forward = form2.save(commit=False)
                forward.byleadengineer = 'yes'
                forward.level = 4
                forward.save()
                messages.success(request, f'New Memo has been forwarded to team ( {project.assignedTo} ) --> {projectEngineer.firstName} {projectEngineer.middleName} !')
                return redirect('le-outgoing-memo')
        else:
            form2 = outgoingMemosForm(instance = obj)
            form = forwardOutMemo(instance = obj, firstName = projectEngineer.firstName, middleName = projectEngineer.middleName)
        try:
            forwardList = DirectorsMemoMessagesOut.objects.filter(subject = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")
            tlforwardList = TeamLeadersMemoMessagesOut.objects.filter(subject = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")
            leforwardList = LeadEngineersMemoMessagesOut.objects.filter(subject = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")
            context = {
                'name' : obj,
                'form2' : form2,
                'form' : form,
                'forwardList' : forwardList,
                'tlforwardList' : tlforwardList,
                'leforwardList' : leforwardList

            }
        except:
            context = {
                'name' : obj,
                'form2' : form2,
                'form' : form,
                'forwardList' : forwardList,
                'tlforwardList' : tlforwardList

            }


        # forward = form2.save(commit=False)
        # forward.byDirector = 'yes'
        # forward.save()
        return render(request, "leadEngineer/forward.html", context)
    else:
        return redirect ('le-outgoing-memo')   