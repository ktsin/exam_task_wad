"""
Definition of forms.
"""

from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import SystemUser


class AuthorizeForm(ModelForm):
    class Meta:
        model = SystemUser
        fields = ['username', 'password']
        labels = {'username': 'Имя пользователя', 'password': 'Пароль'}


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {'username': 'Имя пользователя',
                  'password': 'Пароль'}