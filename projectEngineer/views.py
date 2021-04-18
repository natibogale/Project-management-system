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

from projectEngineer.forms import *
from .models import *

le_login_required = user_passes_test(
    lambda user: True if user.title == 'Project Engineer' and not user.is_admin else False, login_url='/')


def only_pe(view_func):
    decorated_view_func = login_required(
        le_login_required(view_func), login_url='/')
    return decorated_view_func




@only_pe
def projectEngineerHomeView(request):
    return render(request, 'projectEngineer/index.html')    





@only_pe
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
        return render(request, "projectEngineer/update_view.html", context)
    else:
        messages.warning(
            request, f'You have no authorization to access or edit other users profiles!')
        return redirect('project-engineer-home')



@only_pe
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
        return redirect('project-engineer-home')
    else:
        return render(request, "projectEngineer/profile.html", context)


@only_pe
def projectEngineerIncomingLetter(request):
    lists = IncomingLetters.objects.filter(directorate=request.user.directorate, level__gt = 3 ).order_by('byprojectengineer')
    projects = Projects.objects.filter(directorate=request.user.directorate)
    context = {
        'lists' : lists,
        'projects' : projects,
    }
    print('sssssssssssssssssssssssssssssss')
    print(lists)
    return render(request, 'projectEngineer/incoming_letters.html', context)


@only_pe
def projectEngineerIncomingMemo(request):
    lists = IncomingMemos.objects.filter(
        directorate=request.user.directorate, level__gt = 3).order_by('byprojectengineer')
    return render(request, 'projectEngineer/incoming_memos.html', {'lists': lists})

@only_pe
def projectEngineerOutgoingMemo(request):
    lists = OutgoingMemos.objects.filter(
        directorate=request.user.directorate, level__gt = 3).order_by('byprojectengineer')
    return render(request, 'projectEngineer/outgoing_memos.html', {'lists': lists})

@only_pe
def projectEngineerOutgoingLetter(request):
    lists = OutgoingLetters.objects.filter(directorate=request.user.directorate, level__gt = 3 ).order_by('byprojectengineer')
    projects = Projects.objects.filter(directorate=request.user.directorate)
    context = {
        'lists' : lists,
        'projects' : projects,
    }
    return render(request, 'projectEngineer/outgoing_letters.html', context)




@only_pe
def view_projects_list(request):
    projects = Projects.objects.filter(directorate=request.user.directorate, assignedTo=request.user.team, assignedToLE=request.user.id, assignedToPE=request.user.id,).order_by('-dateAdded')
    return render(request, "projectEngineer/projects.html", { 'projects' : projects})


@only_pe
def projectDetails(request, id):
    obj = get_object_or_404(Projects, id = id)
    dire = Projects.objects.filter(id=id, directorate=request.user.directorate, assignedTo=request.user.team, assignedToLE=request.user.id, assignedToPE=request.user.id)
    
    if obj in dire:
        lead_engineer_id = obj.assignedToLE
        le = User.objects.filter(id=lead_engineer_id)
        form = projectDetailsForm(request.POST or None,
                                 request.FILES or None, instance = obj, lead_engineer_id = obj.assignedToLE )
        context = {
            'form': form,
            'name' : obj,
        }
        return render(request, "projectEngineer/project_detail.html", context)
    else:
        messages.warning(
            request, f'You have no authorization to access or edit other directorates projects!')
        return redirect ('pe-projects')




@only_pe
def incomingLettersForward(request, id):
    obj = get_object_or_404(IncomingLetters, id = id)
    dire = IncomingLetters.objects.filter(directorate = request.user.directorate)
    if obj in dire: 
        form2 = incomingLettersForm(instance = obj)
        forward = form2.save(commit=False)
        forward.byprojectengineer = 'yes'
        forward.level = 4
        forward.save()
        try:
            forwardList = DirectorsLetterMessages.objects.filter(referenceNumber = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")
            tlforwardList = TeamLeadersLetterMessages.objects.filter(referenceNumber = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")
            leforwardList = LeadEngineersLetterMessages.objects.filter(referenceNumber = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")
            print('sssssssssssssssssssssssssssssssssssss')
            print(tlforwardList)
            context = {
                'name' : obj,
                # 'form' : form,
                'forwardList' : forwardList,
                'tlforwardList' : tlforwardList,
                'leforwardList' : leforwardList,
            }
        except:

            context = {
                'name' : obj,
                # 'form' : form,
                'forwardList' : forwardList,
                'tlforwardList': tlforwardList,
                'leforwardList': leforwardList,

            }


        # forward = form2.save(commit=False)
        # forward.byDirector = 'yes'
        # forward.save()
        return render(request, "projectEngineer/forward.html", context)
    else:
        return redirect ('pe-incoming-letter')  



@only_pe
def outgoingLettersForward(request, id):
    obj = get_object_or_404(OutgoingLetters, id = id)
    dire = OutgoingLetters.objects.filter(directorate = request.user.directorate)
    if obj in dire: 
        form2 = outgoingLettersForm(instance = obj)
        forward = form2.save(commit=False)
        forward.byprojectengineer = 'yes'
        forward.level = 4
        forward.save()
        try:
            forwardList = DirectorsLetterMessagesOut.objects.filter(referenceNumber = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")
            tlforwardList = TeamLeadersLetterMessagesOut.objects.filter(referenceNumber = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")
            leforwardList = LeadEngineersLetterMessagesOut.objects.filter(referenceNumber = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")
            print('sssssssssssssssssssssssssssssssssssss')
            print(tlforwardList)
            context = {
                'name' : obj,
                # 'form' : form,
                'forwardList' : forwardList,
                'tlforwardList' : tlforwardList,
                'leforwardList' : leforwardList,
            }
        except:

            context = {
                'name' : obj,
                # 'form' : form,
                'forwardList' : forwardList,
                'tlforwardList': tlforwardList,
                'leforwardList' :leforwardList

            }


        # forward = form2.save(commit=False)
        # forward.byDirector = 'yes'
        # forward.save()
        return render(request, "projectEngineer/forward.html", context)
    else:
        return redirect ('pe-outgoing-letter')  







@only_pe
def incomingMemosForward(request, id):
    obj = get_object_or_404(IncomingMemos, id = id)
    dire = IncomingMemos.objects.filter(directorate = request.user.directorate)
    if obj in dire:
        form2 = incomingMemosForm(instance = obj)
        forward = form2.save(commit=False)
        forward.byprojectengineer = 'yes'
        forward.level = 4 
        forward.save()
        try:
            forwardList = DirectorsMemoMessages.objects.filter(subject = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")
            tlforwardList = TeamLeadersMemoMessages.objects.filter(subject = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")
            leforwardList = LeadEngineersMemoMessages.objects.filter(subject = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")

            context = {
                'name' : obj,
                'form2' : form2,
                # 'form' : form,
                'forwardList' : forwardList,
                'tlforwardList' : tlforwardList,
                'leforwardList' : leforwardList,

            }
        except:
            context = {
                'name' : obj,
                'form2' : form2,
                # 'form' : form,
                'forwardList' : forwardList,
                'tlforwardList': tlforwardList,
                'leforwardList' : leforwardList,

            }


        # forward = form2.save(commit=False)
        # forward.byDirector = 'yes'
        # forward.save()
        return render(request, "projectEngineer/forward.html", context)
    else:
        return redirect ('pe-incoming-memo')    

@only_pe
def outgoingMemosForward(request, id):
    obj = get_object_or_404(OutgoingMemos, id = id)
    dire = OutgoingMemos.objects.filter(directorate = request.user.directorate)
    if obj in dire:
        form2 = outgoingMemosForm(instance = obj)
        forward = form2.save(commit=False)
        forward.byprojectengineer = 'yes'
        forward.level = 4 
        forward.save()
        try:
            forwardList = DirectorsMemoMessagesOut.objects.filter(subject = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")
            tlforwardList = TeamLeadersMemoMessagesOut.objects.filter(subject = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")
            leforwardList = LeadEngineersMemoMessagesOut.objects.filter(subject = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")

            context = {
                'name' : obj,
                'form2' : form2,
                # 'form' : form,
                'forwardList' : forwardList,
                'tlforwardList' : tlforwardList,
                'leforwardList' : leforwardList,

            }
        except:
            context = {
                'name' : obj,
                'form2' : form2,
                # 'form' : form,
                'forwardList' : forwardList,
                'tlforwardList': tlforwardList,
                'leforwardList' : leforwardList,

            }


        # forward = form2.save(commit=False)
        # forward.byDirector = 'yes'
        # forward.save()
        return render(request, "projectEngineer/forward.html", context)
    else:
        return redirect ('pe-outgoing-memo')   