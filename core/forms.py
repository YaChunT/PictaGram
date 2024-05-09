# forms.py
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'class': 'bg-gray-200 mb-2 shadow-none dark:bg-gray-800',
            'style': 'border: 1px solid #d3d5d8 !important;'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'bg-gray-200 mb-2 shadow-none dark:bg-gray-800',
            'style': 'border: 1px solid #d3d5d8 !important;'
        })
    )
