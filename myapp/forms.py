from django.db import models
from django import forms


class EntryForm(forms.Form):
    name = forms.CharField(max_length=30)

    date = forms.DateTimeField()
    description= forms.CharField(widget=forms.Textarea)
    lacations = forms.CharField(max_length=30)
    gambar = forms.FileField()
 
