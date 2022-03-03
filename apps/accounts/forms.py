from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django_registration.forms import RegistrationForm


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'E-mail'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )

    class Meta(RegistrationForm.Meta):
        pass


class UserRegistrationForm(RegistrationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'E-mail'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'})
    )

    class Meta(RegistrationForm.Meta):
        model = get_user_model()
