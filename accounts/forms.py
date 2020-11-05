from django import forms
from django.contrib.auth.models import User

from .models import UserProfile

class UserForm(forms.ModelForm):
    confirm_password = forms.CharField(label='Confirme a Senha', max_length=200)  
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'confirm_password']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']
