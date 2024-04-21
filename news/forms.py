from django import forms
from .models import News_Transportation

from ckeditor.widgets import CKEditorWidget

class NewsTransportationForm(forms.ModelForm):
    image = forms.ImageField()
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = News_Transportation
        # fields = ['author_id',]
        exclude = ['author',]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }