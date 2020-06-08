from django import forms
from imageApp.models import Galary

class NameForm(forms.ModelForm):

    class Meta:
        model = Galary
        fields = ('header', 'image')