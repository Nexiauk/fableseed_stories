from django import forms
from .models import Fableseed, Flower

class CreateFableseed(forms.ModelForm):
    flower_type = forms.ModelChoiceField(queryset=Flower.objects.all())
    class Meta:
        model = Fableseed
        fields = (
            'title',
            'body',
            'flower_type'
            )        
form = CreateFableseed()