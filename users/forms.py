from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm


class LoginForm(forms.Form):

    usr = forms.CharField(label='Username')
    pwd = forms.CharField(label='Password', widget=forms.PasswordInput())


class SignUpForm(ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'password', 'email']


