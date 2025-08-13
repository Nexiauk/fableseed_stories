from allauth.account.forms import SignupForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit


class CustomSignupForm(SignupForm):
    display_name = forms.CharField(max_length=70, label="Display Name")

    def save(self, request):
        user = super().save(request)
        user.userprofile.display_name = self.cleaned_data["display_name"]
        user.userprofile.save()
        return user

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("display_name", "bio", "profile_picture")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "CreateFablebranch"
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Field("display_name", css_class="rounded-sm p-2 mb-4 text-gray-700"),
            Field("bio", css_class="rounded-sm p-2 mb-4 text-gray-700"),
            Field("profile_picture", css_class="rounded-sm p-2 mb-4 text-gray-700"),
            Submit("submit", "Submit", css_class="bg-primary mt-4"),
        )
