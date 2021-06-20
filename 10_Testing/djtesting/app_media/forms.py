from django import forms
from .models import File
from django.utils.translation import gettext_lazy as _


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=30, required=False)
    file = forms.FileField(label=_('CSV файл'))


class DocumentForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('description', 'file',)


class MultiFileForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
