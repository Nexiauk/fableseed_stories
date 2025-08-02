from django import forms
from .models import Fableseed

class CreateFableseed(forms.ModelForm):
    class Meta:
        model = Fableseed
        fields = ('body',)