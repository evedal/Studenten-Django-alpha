from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.ModelForm):
    next = forms.CharField(required=False)
    class Meta:
        model = User
        labels = ''
        fields = ['username', 'password']
        widgets = {
        'password': forms.PasswordInput(attrs={'class': 'passwordlogin','placeholder':'Passord'}),
        'username': forms.TextInput(attrs={'class': 'usernamelogin', 'placeholder':'Brukernavn'}),
        }
        labels = {
            "username": "",
            "password": ""
        }

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True, max_length=100)
    first_name = forms.CharField(required=True, max_length=50)
    last_name = forms.CharField(required=True, max_length=50)



    class Meta:
        model = User
        fields = ("username","email","first_name","last_name")


    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.firstname = self.cleaned_data["first_name"]
        user.lastname = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user

class UserEditFirstnameForm(forms.Form):
    first_name = forms.CharField(required=True, max_length=100)
class UserEditLastnameForm(forms.Form):
    last_name = forms.CharField(required=True,max_length=50)
class UserEditEmailForm(forms.Form):
    email = forms.EmailField(required=True,max_length=100)
class UserEditPasswordForm(forms.Form):
    old_password = forms.CharField(required=True,max_length=100)
    new_password1 = forms.CharField(required=True, max_length=100)
    new_password2 = forms.CharField(required=True, max_length=100)
