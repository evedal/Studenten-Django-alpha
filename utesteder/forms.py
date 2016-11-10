from django import forms
from .models import Anmeldelse

class ReviewForm(forms.Form):
    hScore = forms.IntegerField(max_value=5, min_value=1, widget=forms.HiddenInput, initial=0)
    aScore = forms.IntegerField(max_value=5, min_value=0,widget=forms.HiddenInput, initial=0)
    pScore = forms.IntegerField(max_value=5, min_value=0,widget=forms.HiddenInput, initial=0)
    dScore = forms.IntegerField(max_value=5, min_value=0,widget=forms.HiddenInput, initial=0)
    comment = forms.CharField(required=False,label = '',widget=forms.Textarea(attrs=
                                                    {'placeholder': 'Skriv en kommentar!',
                                                     'class':'input-textfield'
                                                 }))




