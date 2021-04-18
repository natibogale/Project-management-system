from bootstrap_datepicker_plus import DatePickerInput
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.shortcuts import (HttpResponseRedirect, get_object_or_404,get_list_or_404,
                              redirect, render)
from django.views.generic import DetailView, UpdateView
from humanResources.forms import profileUpdateForm
from recordOfficer.models import *
from .models import *
from .forms import *
from authentication.models import User
from django.urls import reverse_lazy
from .models import Projects

# from django.http import FileResponse
# from django.shortcuts import get_object_or_404
# from django.views.generic.detail import BaseDetailView

# class DisplayPdfView(BaseDetailView):
#     def get(self, request, *args, **kwargs):
#         objkey = self.kwargs.get('pk', None) #1
#         pdf = get_object_or_404(Pdf, pk=objkey) #2
#         fname = pdf.filename() #3
#         path = os.path.join(settings.MEDIA_ROOT, 'docs\\' + fname)#4
#         response = FileResponse(open(path, 'rb'), content_type="application/pdf")
#         response["Content-Disposition"] = "filename={}".format(fname)
#         return response


dr_login_required = user_passes_test(
    lambda user: True if user.title == 'Director' and not user.is_admin else False, login_url='/')


def only_dr(view_func):
    decorated_view_func = login_required(
        dr_login_required(view_func), login_url='/')
    return decorated_view_func





@only_dr
def directorHomeView(request):
    return render(request, 'director/index.html')




# @only_dr
# def forwardedTo(request):
#     form = forwardMessage()
#
#     return render(request, 'director/incoming_letters.html',{'form',form})


# import schedule
# import time

# def job():
#     print("I'm workingsdfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff")

# schedule.every(5).seconds.do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)


@only_dr
def directorIncomingLetter(request):
    lists = IncomingLetters.objects.filter(directorate=request.user.directorate).order_by('byDirector')
    projects = Projects.objects.filter(directorate=request.user.directorate)
    teamleaders = User.objects.filter(directorate=request.user.directorate, title="Team Leader")
    context = {
        'lists' : lists,
        'projects' : projects,
        'teamleaders' : teamleaders,
    }

    return render(request, 'director/incoming_letters.html', context)




# @only_dr
# def incomingLettersForward(request, id):
#     obj = get_object_or_404(IncomingLetters, id = id)
#     dire = IncomingLetters.objects.filter(directorate = request.user.directorate)
#     forwardedTo = Projects.objects.filter( project = obj.project )
#     if obj in dire:
#     #     form = incomingMemosForm(request.POST or None, instance = obj)
#     #     if form.is_valid():
#     #         ref = form.cleaned_data["subject"]
#     #         form.save()
#     #         messages.success(request, f'Memo { ref } has been updated!')
#     #         return redirect('view-memo-list')
#     #
#     #     context = {
#     #         'form': form,
#     #         'name' : obj,
#     #     }
#     #     return render(request, "recordOfficer/update_view.html", context)
#     # else:
#         return redirect ('view-memo-list')


@only_dr
def directorIncomingMemo(request):
    lists = IncomingMemos.objects.filter(
        directorate=request.user.directorate).order_by('byDirector',)
    return render(request, 'director/incoming_memos.html', {'lists': lists})

@only_dr
def directorOutgoingMemo(request):
    lists = OutgoingMemos.objects.filter(
        directorate=request.user.directorate).order_by('byDirector',)
    return render(request, 'director/outgoing_memos.html', {'lists': lists})

@only_dr
def directorOutgoingLetter(request):
    lists = OutgoingLetters.objects.filter(directorate=request.user.directorate).order_by('byDirector',)
    projects = Projects.objects.filter(directorate=request.user.directorate)
    teamleaders = User.objects.filter(directorate=request.user.directorate, title="Team Leader")
    context = {
        'lists' : lists,
        'projects' : projects,
        'teamleaders' : teamleaders,
    }
    return render(request, 'director/outgoing_letters.html', context)

@only_dr
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
        return render(request, "director/update_view.html", context)
    else:
        messages.warning(
            request, f'You have no authorization to access or edit other users profiles!')
        return redirect('director-home')


@only_dr
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
        return redirect('director-home')
    else:
        return render(request, "director/profile.html", context)




@only_dr
def view_projects_list(request):
    projects = Projects.objects.filter(directorate=request.user.directorate).order_by('-dateAdded')
    return render(request, "director/projects.html", { 'projects' : projects})


@only_dr
def addProjects(request):
    if request.method == 'POST':
        print(request.method)
        form = addProjectsForm(request.POST, request.FILES,director=request.user.directorate)
        if form.is_valid():
            ref = form.cleaned_data['projectName']
            project = form.save(commit=False)
            project.author = request.user
            project.directorate = request.user.directorate
            project.save()
            messages.success(request, f'New Project has been saved!')
            return redirect ('dr-projects')
    else:
        form = addProjectsForm(director=request.user.directorate)
    return render(request, "director/add_projects.html", {'form' : form})


@only_dr
def projectsUpdate(request, id):
    obj = get_object_or_404(Projects, id = id)
    dire = Projects.objects.filter(directorate = request.user.directorate)
    if obj in dire:
        form = editProjects(request.POST or None,
                                 request.FILES or None, instance = obj)
        if form.is_valid():
            ref = form.cleaned_data["projectName"]
            form.save()
            messages.success(request, f'This Project has been updated!')
            return redirect('dr-projects')

        context = {
            'form': form,
            'name' : obj,
        }
        return render(request, "director/update_view.html", context)
    else:
        messages.warning(
            request, f'You have no authorization to access or edit other directorates projects!')
        return redirect ('dr-projects')




@only_dr
def projectsDelete(request, id):
    obj = get_object_or_404(Projects, id = id)
    dire = Projects.objects.filter(directorate = request.user.directorate)
    if obj in dire:
        obj.delete()
        messages.success(request, f'Project    "{ obj }"   has been deleted!')
        return redirect('dr-projects')
    else:
        return redirect('dr-projects')




@only_dr
def incomingLettersForward(request, id):
    obj = get_object_or_404(IncomingLetters, id = id)
    dire = IncomingLetters.objects.filter(directorate = request.user.directorate)
    if obj in dire:
        project = Projects.objects.get( id=obj.project.pk, directorate = request.user.directorate)
        try:
            teamLeader = User.objects.get(directorate = request.user.directorate, title='Team Leader', team=project.assignedTo)
        except:
            messages.warning(request, f"You cannot forward this letter! There is no Team Leader for this Project's assigned team.")
            return redirect ('director-incoming-letter')
        if request.method == 'POST':
            form = forwardMessage(request.POST,firstName = teamLeader.firstName, middleName = teamLeader.middleName,instance = obj )
            form2 = incomingLettersForm(instance = obj)
            if form.is_valid():
                letter = form.save(commit=False)
                letter.author = request.user
                letter.save()
                forward = form2.save(commit=False)
                forward.byDirector = 'yes'
                forward.level = 2
                forward.save()
                messages.success(request, f'New Letter has been forwarded to team ( {project.assignedTo} ) --> {teamLeader.firstName} {teamLeader.middleName} !')
                return redirect('director-incoming-letter')
        else:
            form2 = incomingLettersForm(instance = obj)
            form = forwardMessage(instance = obj, firstName = teamLeader.firstName, middleName = teamLeader.middleName)
        try:
            forwardList = DirectorsLetterMessages.objects.filter(referenceNumber = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")
            context = {
                'name' : obj,
                'form2' : form2,
                'form' : form,
                'forwardList' : forwardList,
            }
        except:
            context = {
                'name' : obj,
                'form2' : form2,
                'form' : form,
            }


        # forward = form2.save(commit=False)
        # forward.byDirector = 'yes'
        # forward.save()
        return render(request, "director/forward.html", context)
    else:
        return redirect ('director-incoming-letter')    






@only_dr
def outgoingLettersForward(request, id):
    obj = get_object_or_404(OutgoingLetters, id = id)
    dire = OutgoingLetters.objects.filter(directorate = request.user.directorate)
    if obj in dire:
        project = Projects.objects.get( id=obj.project.pk, directorate = request.user.directorate)
        try:
            teamLeader = User.objects.get(directorate = request.user.directorate, title='Team Leader', team=project.assignedTo)
        except:
            messages.warning(request, f"You cannot forward this letter! There is no Team Leader for this Project's assigned team.")
            return redirect ('director-outgoing-letter')

        if request.method == 'POST':
            form = forwardOutLetter(request.POST,firstName = teamLeader.firstName, middleName = teamLeader.middleName,instance = obj )
            form2 = outgoingLettersForm(instance = obj)
            if form.is_valid():
                letter = form.save(commit=False)
                letter.author = request.user
                letter.save()
                forward = form2.save(commit=False)
                forward.byDirector = 'yes'
                forward.level = 2
                forward.save()
                messages.success(request, f'New Letter has been forwarded to team ( {project.assignedTo} ) --> {teamLeader.firstName} {teamLeader.middleName} !')
                return redirect('director-outgoing-letter')
        else:
            form2 = outgoingLettersForm(instance = obj)
            form = forwardOutLetter(instance = obj, firstName = teamLeader.firstName, middleName = teamLeader.middleName)
        try:
            forwardList = DirectorsLetterMessagesOut.objects.filter(referenceNumber = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")
            context = {
                'name' : obj,
                'form2' : form2,
                'form' : form,
                'forwardList' : forwardList,
            }
        except:
            context = {
                'name' : obj,
                'form2' : form2,
                'form' : form,
            }


        # forward = form2.save(commit=False)
        # forward.byDirector = 'yes'
        # forward.save()
        return render(request, "director/forward.html", context)
    else:
        return redirect ('director-outgoing-letter')    
    
    
    
@only_dr
def incomingMemosForward(request, id):
    obj = get_object_or_404(IncomingMemos, id = id)
    dire = IncomingMemos.objects.filter(directorate = request.user.directorate)
    if obj in dire:
        project = Projects.objects.get( id=obj.project.pk, directorate = request.user.directorate)
        try:
            teamLeader = User.objects.get(directorate = request.user.directorate, title='Team Leader', team=project.assignedTo)
        except:
            messages.warning(request, f"You cannot forward this Memo! There is no Team Leader for this Project's assigned team.")
            return redirect ('director-incoming-memo')

        if request.method == 'POST':
            form = forwardInMemo(request.POST,firstName = teamLeader.firstName, middleName = teamLeader.middleName,instance = obj )
            form2 = incomingMemosForm(instance = obj)
            if form.is_valid():
                letter = form.save(commit=False)
                letter.author = request.user
                letter.save()
                forward = form2.save(commit=False)
                forward.byDirector = 'yes'
                forward.level = 2
                forward.save()
                messages.success(request, f'New Memo has been forwarded to team ( {project.assignedTo} ) --> {teamLeader.firstName} {teamLeader.middleName} !')
                return redirect('director-incoming-memo')
        else:
            form2 = incomingMemosForm(instance = obj)
            form = forwardInMemo(instance = obj, firstName = teamLeader.firstName, middleName = teamLeader.middleName)
        try:
            forwardList = DirectorsMemoMessages.objects.filter(subject = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")
            context = {
                'name' : obj,
                'form2' : form2,
                'form' : form,
                'forwardList' : forwardList,
            }
        except:
            context = {
                'name' : obj,
                'form2' : form2,
                'form' : form,
            }


        # forward = form2.save(commit=False)
        # forward.byDirector = 'yes'
        # forward.save()
        return render(request, "director/forward.html", context)
    else:
        return redirect ('director-incoming-memo')    




@only_dr
def outgoingMemosForward(request, id):
    obj = get_object_or_404(OutgoingMemos, id = id)
    dire = OutgoingMemos.objects.filter(directorate = request.user.directorate)
    if obj in dire:
        project = Projects.objects.get( id=obj.project.pk, directorate = request.user.directorate)
        try:
            teamLeader = User.objects.get(directorate = request.user.directorate, title='Team Leader', team=project.assignedTo)
        except:
            messages.warning(request, f"You cannot forward this Memo! There is no Team Leader for this Project's assigned team.")
            return redirect ('director-outgoing-memo')

        if request.method == 'POST':
            form = forwardOutMemo(request.POST,firstName = teamLeader.firstName, middleName = teamLeader.middleName,instance = obj )
            form2 = outgoingMemosForm(instance = obj)
            if form.is_valid():
                letter = form.save(commit=False)
                letter.author = request.user
                letter.save()
                forward = form2.save(commit=False)
                forward.byDirector = 'yes'
                forward.level = 2
                forward.save()
                messages.success(request, f'New Memo has been forwarded to team ( {project.assignedTo} ) --> {teamLeader.firstName} {teamLeader.middleName} !')
                return redirect('director-outgoing-memo')
        else:
            form2 = outgoingMemosForm(instance = obj)
            form = forwardOutMemo(instance = obj, firstName = teamLeader.firstName, middleName = teamLeader.middleName)
        try:
            forwardList = DirectorsMemoMessagesOut.objects.filter(subject = obj.pk).exclude(message =  "Message" ).order_by("-dateSent")
            context = {
                'name' : obj,
                'form2' : form2,
                'form' : form,
                'forwardList' : forwardList,
            }
        except:
            context = {
                'name' : obj,
                'form2' : form2,
                'form' : form,
            }


        # forward = form2.save(commit=False)
        # forward.byDirector = 'yes'
        # forward.save()
        return render(request, "director/forward.html", context)
    else:
        return redirect ('director-outgoing-memo')    



@only_dr
def projectDetails(request, id):
    obj = get_object_or_404(Projects, id = id)
    dire = Projects.objects.filter(directorate = request.user.directorate)
    if obj in dire:
        form = projectDetailsForm(request.POST or None,
                                 request.FILES or None, instance = obj)
        context = {
            'form': form,
            'name' : obj,
        }
        return render(request, "director/project_detail.html", context)
    else:
        messages.warning(
            request, f'You have no authorization to access or edit other directorates projects!')
        return redirect ('dr-projects')