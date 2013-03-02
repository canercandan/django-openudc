# -*- coding: utf-8 -*-
from django import forms

class Add(forms.Form):
    keytext = forms.CharField(label="",
                              widget=forms.Textarea(attrs={'class': 'span12',
                                                           'placeholder': 'Paste your public key here',}
                                                    )
                              )

class Lookup(forms.Form):
    search = forms.CharField(max_length=255)
