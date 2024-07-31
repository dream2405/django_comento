from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, max_length=100)


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = (
            "username",
            "password1",
            "password2",
            "email"
        )

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 6:
            raise ValidationError("idLengthError")
        return username

    def clean_password1(self):
        password = self.cleaned_data['password1']
        if len(password) < 8:
            raise ValidationError("pwLengthError")
        return password
