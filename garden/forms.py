"""
Forms for user signup and profile editing in the Fableseed app.

Includes:
- CustomSignupForm: Extends allauth SignupForm to include display_name.
- EditProfileForm: Allows editing of a user's display name, bio, and profile picture.
"""

from allauth.account.forms import SignupForm
from django import forms
from .models import UserProfile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit


class CustomSignupForm(SignupForm):
    """
    Custom signup form that extends allauth's SignupForm to include
    a 'display_name' field and save it to the associated UserProfile.
    """
    display_name = forms.CharField(max_length=70, label="Display Name")

    def save(self, request):
        """
        Save the user and assign the display_name to the related UserProfile.
        """
        user = super().save(request)
        user.userprofile.display_name = self.cleaned_data["display_name"]
        user.userprofile.save()
        return user


class EditProfileForm(forms.ModelForm):
    """
    Form for editing an existing user's profile.

    """
    class Meta:
        model = UserProfile
        fields = ("display_name", "bio", "profile_picture")

    def __init__(self, *args, **kwargs):
        """
        Initialize the form and set up Crispy Forms helper for styling.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "edit-profile"
        self.helper.form_method = "post"
        self.helper.form_enctype = 'multipart/form-data'
        self.helper.layout = Layout(
            Field(
                "display_name",
                css_class="rounded-sm p-2 mb-4 text-gray-700"
            ),
            Field("bio",
                  css_class="rounded-sm p-2 mb-4 text-gray-700"
                  ),
            Field("profile_picture",
                  css_class=(
                      "btn bg-primary hover:bg-secondary"
                      "hover:text-secondary-content"
                      )
                  ),
            Submit("submit",
                   "Submit",
                   css_class=(
                       "btn bg-primary mt-4 "
                       "hover:bg-secondary hover:text-secondary-content"
                       )
                   ),
        )
