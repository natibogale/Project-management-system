from authentication.models import User
# from bootstrap_datepicker_plus import DatePickerInput
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import (HttpResponseRedirect, get_object_or_404,
                              redirect, render)
from django.views.generic import DetailView, UpdateView
from humanResources.forms import profileUpdateForm

from .forms import *
from .models import *





# user_login_required = user_passes_test(lambda user: not user.is_admin, login_url='/')

# def not_admin(view_func):
#     decorated_view_func = login_required(user_login_required(view_func))
#     return decorated_view_func




ro_login_required = user_passes_test(lambda user: True if user.title == 'Record Officer' and not user.is_admin else False, login_url='/')

def only_ro(view_func):
    decorated_view_func = login_required(ro_login_required(view_func), login_url='/')
    return decorated_view_func






#@login_required@
@only_ro
def roHomeView(request):
    if request.method == 'POST':
        form = UpdateProfile(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('record-officer')
    else:
        return render(request, 'recordOfficer/index.html')



@only_ro
def letter_in_detail(DetailView):
    model = IncomingLetters
    template_name = 'recordOfficer/update_letters_in.html'


@only_ro
def incomingLettersUpdate(request, id):
    obj = get_object_or_404(IncomingLetters, id = id)
    dire = IncomingLetters.objects.filter(directorate = request.user.directorate)
    if obj in dire:
        form = incomingLettersForm(request.POST or None, instance = obj)
        if form.is_valid():
            ref = form.cleaned_data["referenceNumber"]
            form.save()
            messages.success(request, f'Letter { ref } has been updated!')
            return redirect('view-letter-list')

        context = {
            'form': form,
            'name' : obj,
        }
        return render(request, "recordOfficer/update_view.html", context)
    else:
        return redirect ('view-letter-list')



@only_ro
def incomingMemosUpdate(request, id):
    obj = get_object_or_404(IncomingMemos, id = id)
    dire = IncomingMemos.objects.filter(directorate = request.user.directorate)
    if obj in dire:
        form = incomingMemosForm(request.POST or None, instance = obj)
        if form.is_valid():
            ref = form.cleaned_data["subject"]
            form.save()
            messages.success(request, f'Memo { ref } has been updated!')
            return redirect('view-memo-list')

        context = {
            'form': form,
            'name' : obj,
        }
        return render(request, "recordOfficer/update_view.html", context)
    else:
        return redirect ('view-memo-list')



@only_ro
def outgoingMemosUpdate(request, id):
    obj = get_object_or_404(OutgoingMemos, id = id)
    dire = OutgoingMemos.objects.filter(directorate = request.user.directorate)
    if obj in dire:
        form = outgoingMemosForm(request.POST or None, instance = obj)
        if form.is_valid():
            ref = form.cleaned_data["subject"]
            form.save()
            messages.success(request, f'Memo { ref } has been updated!')
            return redirect('view-memo-out')

        context = {
            'form': form,
            'name' : obj,
        }
        return render(request, "recordOfficer/update_view.html", context)
    else:
        return redirect ('view-memo-out')







@only_ro
def incomingMemosDelete(request, id):
    obj = get_object_or_404(IncomingMemos, id = id)
    dire = IncomingMemos.objects.filter(directorate = request.user.directorate)
    if obj in dire:
        obj.delete()
        messages.success(request, f'Memo { obj } has been deleted!')
        return redirect('view-memo-list')
    else:
        return redirect('view-memo-list')



@only_ro
def outgoingMemosDelete(request, id):
    obj = get_object_or_404(OutgoingMemos, id = id)
    dire = OutgoingMemos.objects.filter(directorate = request.user.directorate)
    if obj in dire:
        obj.delete()
        messages.success(request, f'Memo { obj } has been deleted!')
        return redirect('view-memo-out')
    else:
        return redirect('view-memo-out')


@only_ro
def outgoingLettersUpdate(request, id):
    obj = get_object_or_404(OutgoingLetters, id = id)
    dire = OutgoingLetters.objects.filter(directorate = request.user.directorate)
    if obj in dire:
        form = outgoingLettersForm(request.POST or None, instance = obj)
        if form.is_valid():
            ref = form.cleaned_data["referenceNumber"]
            form.save()
            messages.success(request, f'Letter { ref } has been updated!')
            return redirect('view-letter-out')

        context = {
            'form': form,
            'name' : obj,
        }
        return render(request, "recordOfficer/update_view.html", context)

    else:
        return redirect ('view-letter-out')





@only_ro
def incomingLettersDelete(request, id):
    obj = get_object_or_404(IncomingLetters, id = id)
    dire = IncomingLetters.objects.filter(directorate = request.user.directorate)
    if obj in dire:
        obj.delete()
        messages.success(request, f'Letter { obj } has been deleted!')
        return redirect('view-letter-list')
    else:
        return redirect('view-letter-list')



@only_ro
def outgoingLettersDelete(request, id):
    obj = get_object_or_404(OutgoingLetters, id = id)
    dire = OutgoingLetters.objects.filter(directorate = request.user.directorate)
    if obj in dire:
        obj.delete()
        messages.success(request, f'Letter { obj } has been deleted!')
        return redirect('view-letter-out')
    else:
        return redirect('view-letter-out')


@only_ro
def insert_letters_in(request):
    if request.method == 'POST':
        print(request.method)
        form = incomingLettersForm(request.POST, request.FILES)
        if form.is_valid():
            ref = form.cleaned_data['referenceNumber']
            letter = IncomingLetters()
            letter.subject = form.cleaned_data['subject']
            letter.referenceNumber = form.cleaned_data['referenceNumber']
            letter.dateWritten = request.POST.get('dateWritten')
            letter.dateReceived = request.POST.get('dateReceived')
            letter.signatore = form.cleaned_data['signatore']
            letter.receivedFrom = form.cleaned_data['receivedFrom']
            letter.cc = form.cleaned_data['cc']
            letter.project = form.cleaned_data['project']
            letter.type = form.cleaned_data['type']
            letter.pageNumber = form.cleaned_data['pageNumber']
            letter.file    = request.FILES['file']
            letter.author = request.user.username
            letter.directorate = request.user.directorate
            letter.save()
            messages.success(request, f'Letter { ref } has been saved!')
            return redirect ('view-letter-list')
    else:
            form = incomingLettersForm()
    return render(request, 'recordOfficer/insert_letters_in.html', { 'form' : form} )



@only_ro
def insert_memo_in(request):
    if request.method == 'POST':
        form = incomingMemosForm(request.POST, request.FILES)
        if form.is_valid():
            sub = form.cleaned_data['subject']
            letter = IncomingMemos()
            letter.subject = form.cleaned_data['subject']
            letter.dateWritten = request.POST.get('dateWritten')
            letter.signatore = form.cleaned_data['signatore']
            letter.receivedFrom = form.cleaned_data['receivedFrom']
            letter.cc = form.cleaned_data['cc']
            letter.project = form.cleaned_data['project']
            letter.pageNumber = form.cleaned_data['pageNumber']
            letter.file    = request.FILES['file']
            letter.author = request.user.username
            letter.directorate = request.user.directorate
            letter.save()
            messages.success(request, f'Memo { sub } has been saved!')
            return redirect ('view-memo-list')
    else:
        form = incomingMemosForm()
    return render(request, 'recordOfficer/insert_memo_in.html', { 'form' : form})



@only_ro
def insert_memo_out(request):
    if request.method == 'POST':
        form = outgoingMemosForm(request.POST, request.FILES)
        if form.is_valid():
            sub = form.cleaned_data['subject']
            letter = OutgoingMemos()
            letter.subject = form.cleaned_data['subject']
            letter.dateWritten = request.POST.get('dateWritten')
            letter.signatore = form.cleaned_data['signatore']
            letter.sentTo = form.cleaned_data['sentTo']
            letter.cc = form.cleaned_data['cc']
            letter.project = form.cleaned_data['project']
            letter.pageNumber = form.cleaned_data['pageNumber']
            letter.file    = request.FILES['file']
            letter.author = request.user.username
            letter.directorate = request.user.directorate
            letter.save()
            messages.success(request, f'Memo { sub } has been saved!')
            return redirect ('view-memo-out')
    else:
        form = outgoingMemosForm()
    return render(request, 'recordOfficer/insert_memo_out.html', { 'form' : form})


@only_ro
def view_memo_list(request):
    memos = IncomingMemos.objects.filter(directorate=request.user.directorate).order_by('-dateAdded')
    return render(request, 'recordOfficer/view_memo_list.html', { 'memos' : memos})

@only_ro
def view_memo_out(request):
    memos = OutgoingMemos.objects.filter(directorate=request.user.directorate).order_by('-dateAdded')
    return render(request, 'recordOfficer/view_memo_out.html', { 'memos' : memos})

@only_ro
def view_letter_list(request):
    lists = IncomingLetters.objects.filter(directorate=request.user.directorate).order_by('-dateAdded')
    return render(request, 'recordOfficer/view_letter_list.html', { 'lists' : lists})

@only_ro
def view_letter_out(request):
    lists = OutgoingLetters.objects.filter(directorate=request.user.directorate).order_by('-dateAdded')
    return render(request, 'recordOfficer/view_letter_out.html', { 'lists' : lists})



@only_ro
def insert_letters_out(request):
    if request.method == 'POST':
        form = outgoingLettersForm(request.POST, request.FILES)
        if form.is_valid():
            ref = form.cleaned_data['referenceNumber']
            letter = OutgoingLetters()
            letter.subject = form.cleaned_data['subject']
            letter.referenceNumber = form.cleaned_data['referenceNumber']
            letter.dateWritten = request.POST.get('dateWritten')
            letter.dateDelivered = request.POST.get('dateDelivered')
            letter.signatore = form.cleaned_data['signatore']
            letter.sentTo = form.cleaned_data['sentTo']
            letter.cc = form.cleaned_data['cc']
            letter.project = form.cleaned_data['project']
            letter.type = form.cleaned_data['type']
            letter.pageNumber = form.cleaned_data['pageNumber']
            letter.file    = request.FILES['file']
            letter.author = request.user.username
            letter.directorate = request.user.directorate
            letter.save()
            messages.success(request, f'Letter { ref } has been saved!')
            return redirect ('view-letter-out')
    else:
        form = outgoingLettersForm()
    return render(request, 'recordOfficer/insert_letters_out.html', { 'form' : form})


@only_ro
def userProfileUpdate(request, id):
    obj = get_object_or_404(User, id = id)
    dire = User.objects.filter(username = request.user)
    if obj in dire:
        form = profileUpdateForm(request.POST or None,  request.FILES or None, instance = obj)
        if form.is_valid():
            ref = form.cleaned_data["username"]
            form.save()
            messages.success(request, f'"{ ref }"   your profile has been updated!')
            url = request.get_full_path()
            this = url.replace('update', '')
            return redirect(this)

        context = {
            'form': form,
            'name' : obj,
        }
        return render(request, "recordOfficer/update_view.html", context)
    else:
        messages.warning(request,f'You have no authorization to access or edit other users profiles!')
        return redirect('record-officer-home')


@only_ro
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
        return redirect('record-officer-home')
    else:
        return render(request, "recordOfficer/profile.html", context)
