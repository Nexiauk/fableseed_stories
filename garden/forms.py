from allauth.account.forms import SignupForm
from django import forms
from .models import UserProfile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit


class CustomSignupForm(SignupForm):
    """
    Custom signup form that extends allauth's SignupForm to include
    a 'display_name' field and save it to the associated UserProfile.

    Attributes:
        display_name (CharField): Public name displayed for the user.

    Methods:
        save(request): Saves the user and updates the UserProfile with the
                       cleaned display_name.
    """
    display_name = forms.CharField(max_length=70, label="Display Name")

    def save(self, request):
        """
        Save the user and assign the display_name to the related UserProfile.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            User: The newly created user instance.
        """
        user = super().save(request)
        user.userprofile.display_name = self.cleaned_data["display_name"]
        user.userprofile.save()
        return user


class EditProfileForm(forms.ModelForm):
    """
    Form for editing an existing user's profile.

    Attributes:
        Meta: Specifies the model and fields included in the form.
        helper (FormHelper): Configures Crispy Forms layout and styling.

    Methods:
        __init__(*args, **kwargs): Initializes the form and applies
        Crispy Forms styling and layout.
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
