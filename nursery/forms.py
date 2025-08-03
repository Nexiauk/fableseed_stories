from django import forms
from .models import Fableseed, Flower
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit


class CreateFableseed(forms.ModelForm):
    flower_type = forms.ModelChoiceField(queryset=Flower.objects.all())

    class Meta:
        model = Fableseed
        fields = ("title", "body", "flower_type")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "createFableseed"
        self.helper.form_method = "post"
        self.helper.add_input(Submit('submit', 'Submit', css_class="mt-4"))
        self.helper.layout = Layout(
            Field("title", css_class="mb-4"),
            Field("body", css_class="mb-4"),
            Field("flower_type", css_class="mt-4"),
        )
