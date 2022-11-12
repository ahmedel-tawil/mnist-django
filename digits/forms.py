from django import forms

from digits.models import Digits


class UploadForm(forms.ModelForm):
    class Meta:
        model = Digits
        fields = ['image']
