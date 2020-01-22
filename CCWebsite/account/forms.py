from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import ExtendedUserModel
from account.models import ExtendedUserModel


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserExtendedForm(forms.ModelForm):
    class Meta:
        model = ExtendedUserModel
        fields = ['phone_number', 'age', 'location', 'gender']


class LoginForm(forms.ModelForm):
    class Meta:
        model= User
        fields=['username','password']

class EditForm(forms.ModelForm):
    class Meta:
        model= ExtendedUserModel
        fields=[
            'age',
            'gender',
            'location',
            'phone_number',
        ]
    def clean(self):
        return self.cleaned_data