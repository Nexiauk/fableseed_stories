from django import forms
from .models import Fableseed, Flower
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit

class CreateFableseed(forms.ModelForm):
    flower_type = forms.ModelChoiceField(queryset=Flower.objects.all())
    class Meta:
        model = Fableseed
        fields = (
            'title',
            'body',
            'flower_type'
            )        


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = "border p-8"
        self.helper.layout = Layout(
            Div(
                Div('title', css_class="md:w-[50%]"),
                Div('body', css_class="md:w-[50%]" ),
        ),
        'flower_type',
        Submit('submit', 'Submit', css_class='text-white bg-blue-700'),
        )