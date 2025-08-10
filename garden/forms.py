from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    display_name = forms.CharField(max_length=70, label='Display Name')

    def save(self, request):
        user = super().save(request)
        user.userprofile.display_name = self.cleaned_data['display_name']
        user.userprofile.save()
        return user