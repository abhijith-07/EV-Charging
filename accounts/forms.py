from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from allauth.account.forms import LoginForm, SignupForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        #fields = '__all__'
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class CustomLoginForm(LoginForm):
    class Meta:
        model = User
        fields = '__all__'

class CustomSignupForm(SignupForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']