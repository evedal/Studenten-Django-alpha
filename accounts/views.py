from django.shortcuts import render
from .forms import UserEditEmailForm,UserEditLastnameForm,UserEditFirstnameForm,UserEditPasswordForm
from hjem import views
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.exceptions import ValidationError
from django.core.context_processors import csrf
from django.contrib.auth import views
from django.contrib.auth import forms
from Studenten.settings import LOGIN_URL

from .forms import UserCreateForm as UCF

userinfoEditSuccess = 'Din brukerinformasjon er endret!'
userinfoEditFailure = 'En feil har oppstått og din brukerinformasjon er ikke endret!'
userEmailCreateFailure = "E-post adressen er allerede registrert."

def auth_view(request):
    if request.method == 'POST':
        received_form = forms.AuthenticationForm(data=request.POST)
        try:
            if received_form.is_valid():
                username = received_form.data['username']
                password = received_form.data['password']
                user = auth.authenticate(username=username,password=password)
                if user is not None:
                    auth.login(request,user)
                    if request.POST["next"] != "":
                        return HttpResponseRedirect(request.POST["next"])
                    else:
                        return HttpResponseRedirect('/accounts/success/')
                else:
                    raise ValidationError(received_form.errors)
            else:
                raise ValidationError(received_form.errors)
        except ValidationError as v:
            return login(request, error_message=v.__str__())
    else:
        return HttpResponseRedirect(LOGIN_URL)



def login(request, error_message = None):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/accounts/profile/")
    if error_message is not None:
        return render(request, 'accounts/login.html', {'form': forms.AuthenticationForm,'error_message':error_message,'request':request})
    else:
        return render(request,'accounts/login.html', {'form':forms.AuthenticationForm,'request':request})

def register(request):
    form = UCF
    if request.method == "POST":
        try:
            user = form(request.POST)
            if user.is_valid():
                user.save()
                user = auth.authenticate(username=request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return HttpResponseRedirect('/hjem/')
            else:
                raise ValidationError(user.errors)
        except ValidationError as v:
            return render(request,'accounts/register.html',{'form':form,'error_message': v.__str__})
    else:
        return render(request,'accounts/register.html',{'form':form})

def success(request):
    return HttpResponseRedirect('/hjem/')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/hjem/')

def forgot(request):
    return views.password_reset(request, template_name='accounts/forgot.html')

def emailsent(request):
    return views.password_change_done(request,template_name='accounts/emailsent.html')

def profile(request, return_message = ''):
    user = request.user
    auth = None
    if user.is_authenticated():
        auth = user
        return render(request,'accounts/profile.html',{'auth':auth, 'return_message':return_message})
    else:
        return HttpResponseRedirect('/accounts/')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return HttpResponseRedirect("/accounts/")
    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect("/accounts/profile/")
        else:
            return HttpResponseRedirect("/hjem/")


#TODO: DETTE MÅ FIKSES
def edit_firstname(request):
    user = request.user
    if user.is_authenticated():
        if request.method == 'POST':
            form = UserEditFirstnameForm(request.POST)
            if form.is_valid():
                input = form.data['first_name']
                user.first_name = input
                user.save()
                return profile(request,return_message=userinfoEditSuccess)
    return profile(request,return_message=userinfoEditFailure)

def edit_lastname(request):
    user = request.user
    if user.is_authenticated():
        if request.method == 'POST':
            form = UserEditLastnameForm(request.POST)
            if form.is_valid():
                input = form.data['last_name']
                user.last_name = input
                user.save()
                return profile(request,return_message=userinfoEditSuccess)
    return profile(request,return_message=userinfoEditFailure)

def edit_email(request):
    user = request.user
    if user.is_authenticated():
        if request.method == 'POST':
            form = UserEditEmailForm(request.POST)
            if form.is_valid():
                input = form.data['email']
                user.email = input
                user.save()
                return profile(request,return_message=userinfoEditSuccess)
    return profile(request,return_message=userinfoEditFailure)

def edit_password(request):
    user = request.user
    if user.is_authenticated():
        if request.method == 'POST':
            form = UserEditPasswordForm(request.POST)
            if form.is_valid():
                if form.data['new_password1'] == form.data['new_password2']:
                    if request.user.check_password(form.data['old_password']):
                        request.user.set_password(form.data['new_password1'])
                        user.save()
                        return profile(request,return_message=userinfoEditSuccess)
    return profile(request,return_message=userinfoEditFailure)