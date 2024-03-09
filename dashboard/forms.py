from django import forms
from transportation.models import *

class Transportation_Air_Form(forms.ModelForm):
    image = forms.ImageField()
    class Meta:
        model = Transportation_Air
        fields = [
            'body',
            'image',
        ]

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class Transportation_Road_Form(forms.ModelForm):
    image = forms.ImageField()
    class Meta:
        model = Transportation_Road
        fields = [
            'body',
            'image',
        ]

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class Transportation_Maritime_Form(forms.ModelForm):
    image = forms.ImageField()
    class Meta:
        model = Transportation_Maritime
        fields = [
            'body',
            'image',
        ]

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class Transportation_About_Form(forms.ModelForm):
    class Meta:
        model = Transportation_About
        fields = [
            'body',
        ]

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class Transportation_Members_Form(forms.ModelForm):
    image = forms.ImageField()
    class Meta:
        model = Transportation_Members
        fields = [
            'fullname',
            'body',
            'status',
            'image',
        ]

        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class Transportation_Certificate_Form(forms.ModelForm):
    image = forms.ImageField()
    class Meta:
        model = Transportation_Certificate
        fields = [
            'name',
            'status',
            'image',
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }