"""
Django forms for creating and editing Fableseed and FableBranch objects.
Includes forms for planting seeds, growing branches, and editing existing content.
"""

from django import forms
from .models import Fableseed, Flower, FableBranch
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Button


class CreateFableseed(forms.ModelForm):
    """
    Form for creating a new Fableseed.
    Includes title, body, and flower type fields.
    """
    flower_type = forms.ModelChoiceField(queryset=Flower.objects.all())

    class Meta:
        model = Fableseed
        fields = ("title", "body", "flower_type")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["flower_type"].label = "Flower Type"
        self.helper = FormHelper()
        self.helper.form_id = "create-fableseed"
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Field(
                "title",
                css_class="rounded-sm p-2 mb-4 text-gray-700",
                placeholder="Enter your Fableseed title here..."
            ),
            Field(
                "body",
                css_class="rounded-sm p-2 mb-4 text-gray-700",
                placeholder="Write your story starter here..."
            ),
            Field("flower_type"),
            Button(
                "back",
                "Back",
                css_class=(
                    "bg-primary mt-4 hover:bg-secondary hover:text-secondary-content"
                ),
                onclick="history.back()"
            ),
            Submit(
                "submit",
                "Plant Seed",
                css_class=(
                    "bg-primary mt-4 hover:bg-secondary hover:text-secondary-content"
                ),
            ),
        )


class CreateFablebranch(forms.ModelForm):
    """
    Form for creating a new FableBranch.
    Includes only the body field for user input.
    """
    class Meta:
        model = FableBranch
        fields = ("body",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "create-fablebranch"
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Field(
                "body",
                css_class="rounded-sm p-2 mb-4 text-gray-700"
            ),
            Button(
                "back",
                "Back",
                css_class=(
                    "bg-primary mt-4 hover:bg-secondary hover:text-secondary-content"
                ),
                onclick="history.back()"
            ),
            Submit(
                "submit",
                "Grow Branch",
                css_class=(
                    "bg-primary mt-4 hover:bg-secondary hover:text-secondary-content"
                ),
            ),
        )


class EditFablebranch(forms.ModelForm):
    """
    Form for editing an existing FableBranch.
    Includes only the body field for user edits.
    """
    class Meta:
        model = FableBranch
        fields = ("body",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "edit-fablebranch"
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Field(
                "body",
                css_class="rounded-sm p-2 mb-4 text-gray-700"
            ),
            Button(
                "back",
                "Back",
                css_class=(
                    "bg-primary mt-4 hover:bg-secondary hover:text-secondary-content"
                ),
                onclick="history.back()"
            ),
            Submit(
                "submit",
                "Tend",
                css_class=(
                    "bg-primary mt-4 hover:bg-secondary hover:text-secondary-content"
                ),
            ),
        )


class EditFableseed(forms.ModelForm):
    """
    Form for editing an existing Fableseed.
    Allows editing title, body, and flower type fields.
    """
    flower_type = forms.ModelChoiceField(queryset=Flower.objects.all())

    class Meta:
        model = Fableseed
        fields = ("title", "body", "flower_type")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["flower_type"].label = "Flower Type"
        self.helper = FormHelper()
        self.helper.form_id = "edit-fableseed"
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Field(
                "title",
                css_class="rounded-sm p-2 mb-4 text-gray-700"
            ),
            Field(
                "body",
                css_class="rounded-sm p-2 mb-4 text-gray-700"
            ),
            Field("flower_type"),
            Button(
                "back",
                "Back",
                css_class=(
                    "bg-primary mt-4 hover:bg-secondary hover:text-secondary-content"
                ),
                onclick="history.back()"
            ),
            Submit(
                "submit",
                "Tend",
                css_class=(
                    "bg-primary mt-4 hover:bg-secondary hover:text-secondary-content"
                ),
            ),
        )
