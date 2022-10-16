from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    email = forms.EmailField()
    username = forms.CharField(max_length=25)
    password = forms.CharField(max_length=40)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'first_name', 'last_name']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(max_length=40)
 