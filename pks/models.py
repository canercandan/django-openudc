# -*- coding: utf-8 -*-
from django import forms

# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
# from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class Add(forms.Form):
    keytext = forms.CharField(label="",
                              widget=forms.Textarea(attrs={'class': 'span12',
                                                           'placeholder': 'Paste your public key here',}
                                                    )
                              )

    # helper = FormHelper()
    # helper.form_class = 'form-pks span12'
    # helper.layout = Layout(
    #     Field('keytext', css_class='input-xlarge span12'),
    #     FormActions(
    #         Submit('update', 'Add or Update', css_class="btn-large"),
    #         ),
    #     )

class Lookup(forms.Form):
    search = forms.CharField(max_length=255)

    # helper = FormHelper()
    # helper.form_class = 'navbar-search pull-right'
    # helper.layout = Layout(
    #     Field('search', css_class='search-query', placeholder='Search a key'),
    #     )
