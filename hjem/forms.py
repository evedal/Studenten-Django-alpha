from django import forms
from . import models
class BrukerForm(forms.ModelForm):
    class Meta:
        model = models.Bruker
        widgets = {
        'password': forms.PasswordInput(),
        }