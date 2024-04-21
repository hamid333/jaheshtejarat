from django import forms
from transportation.models import *

from ckeditor.widgets import CKEditorWidget


class Transportation_Air_Form(forms.ModelForm):
    image = forms.ImageField()
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Transportation_Air
        fields = '__all__'


class Transportation_Road_Form(forms.ModelForm):
    image = forms.ImageField()
    body = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Transportation_Road
        fields = '__all__'



class Transportation_Maritime_Form(forms.ModelForm):
    image = forms.ImageField()
    body = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Transportation_Maritime
        fields = '__all__'




class Transportation_About_Form(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Transportation_About
        fields = '__all__'



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
