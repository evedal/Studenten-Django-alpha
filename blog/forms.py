from django import forms
from . import models
class CommentForm(forms.Form):
    body = forms.CharField(required=True,label = '',widget=forms.Textarea(attrs=
                                                    {'placeholder': 'Skriv en kommentar!',
                                                     'class':'addcomment_text'
                                                 }))