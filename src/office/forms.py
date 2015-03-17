from django import forms
from .models import Office
from django.forms import ModelForm


class OfficeDetailsForm(forms.Form):

    query = forms.CharField(max_length=30, required=True)
    city = forms.CharField(max_length=60, required=True)
