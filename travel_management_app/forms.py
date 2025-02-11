from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)


class Signupform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']