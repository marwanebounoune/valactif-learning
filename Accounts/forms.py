from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from Accounts import models



""" class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Old Password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Passowrd'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Conform new password'}))
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2'] """
                



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email','first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['tel1','tel2','genre','dateNaissance','country', 'photoProfile','username', 'email','first_name', 'last_name']