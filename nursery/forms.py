from django import forms
from .models import Fableseed, Flower
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div, Submit


class CreateFableseed(forms.ModelForm):
    flower_type = forms.ModelChoiceField(
        queryset=Flower.objects.all()
    )

    class Meta:
        model = Fableseed
        fields = ("title", "body", "flower_type")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["flower_type"].label = "Flower Type"
        self.helper = FormHelper()
        self.helper.form_id = "createFableseed"
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Field("title", css_class="rounded-sm p-2 mb-4 text-primary-content"),
            Field("body", css_class="rounded-sm p-2 mb-4 text-primary-content"),
            Field("flower_type"),
            Submit("submit", "Submit", css_class="bg-primary mt-4"),
        )
