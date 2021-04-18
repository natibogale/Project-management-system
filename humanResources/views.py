from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import registrationForm
from .models import *
from authentication.models import *
from authentication.models import User as usmodel
from django.views.generic import DetailView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import (HttpResponseRedirect, get_object_or_404,
                              redirect, render)
from .forms import *

# def is_hr(self):
#     if str(self.title) == 'HR Officer':
#         return True
#     else:
#         return False


hr_login_required = user_passes_test(lambda user: True if user.title == 'HR Officer' and not user.is_admin else False, login_url='/')


def only_hr(view_func):
    decorated_view_func = login_required(hr_login_required(view_func), login_url='/')
    return decorated_view_func




# user_login_required = user_passes_test(lambda user: not user.is_admin, login_url='/')

# def not_admin(view_func):
#     decorated_view_func = login_required(user_login_required(view_func))
#     return decorated_view_func


@only_hr
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
        return render(request, "humanResources/update_view.html", context)
    else:
        messages.warning(
            request, f'You have no authorization to access or edit other users profiles!')
        return redirect('human-resources-home')


@only_hr
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
        return redirect('human-resources-home')
    else:
        return render(request, "humanResources/profile.html", context)






@only_hr
def registrationView(request):
    if request.POST:
        form = registrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # auth = authenticate(username=username, password=password)
            # login(request,auth)
            messages.success(request, f'The Account is succesfully created user { username } now has access!')
            return redirect('hr-employees-list')
        # else:
        #     # form = registrationForm(request.POST, request.FILES)

    else:
        form = registrationForm()
    return render(request, 'humanResources/register_employees.html', { 'form' : form})


@only_hr
def hrHomeView(request):
    return render(request, 'humanResources/index.html')

# @not_admin
@only_hr
def employeesList(request):
    users = User.objects.all().order_by('-date_joined')
    return render(request, 'humanResources/employees_list.html',{ 'users' : users})

# @not_admin
# @only_hr



@method_decorator(only_hr, name='dispatch')
class employeesUpdate(SuccessMessageMixin, UpdateView):
    model = usmodel
    fields = ['username', 'firstName', 'middleName', 'lastName','email', 'phoneNumber','directorate','team','title',
              'emergencyContactName','emergencyContactPhone', ]
    template_name = 'humanResources/employees_update.html'
    # def get_success_url(self):
    #     messages.success(request, f'The Account has been succesfully updated!')
    #     return reverse('hr-employees-list')
    success_url = reverse_lazy('hr-employees-list')
    success_message = "The Account has been succesfully updated!"
