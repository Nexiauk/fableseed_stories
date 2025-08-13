from allauth.account.forms import SignupForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile

class CustomSignupForm(SignupForm):
    display_name = forms.CharField(max_length=70, label='Display Name')

    def save(self, request):
        user = super().save(request)
        user.userprofile.display_name = self.cleaned_data['display_name']
        user.userprofile.save()
        return user
    
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("display_name", "bio", "profile_picture")
