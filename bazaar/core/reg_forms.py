from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SigninForm(AuthenticationForm):
    username = forms.CharField( widget= forms.TextInput(attrs = {
            "class" : "w-11/12 p-4 rounded-lg",
            "placeholder": "Please enter name"
        }))
    password = forms.CharField( widget=forms.PasswordInput(attrs= {
        "class" : "w-11/12 p-4 rounded-lg",
        "placeholder": "Please enter password"
    }))

class RegisterationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    username = forms.CharField( widget= forms.TextInput(attrs = {
            "class" : "w-11/12 p-4 rounded-lg",
            "placeholder": "Please enter name"
        }))
    email = forms.CharField( widget=forms.EmailInput(
        attrs= {
            "class" : "w-11/12 p-4 rounded-lg",
            "placeholder": "Please enter email"
        }))
    password1 = forms.CharField( widget=forms.PasswordInput(attrs= {
        "class" : "w-11/12 p-4 rounded-lg",
        "placeholder": "Please enter password"
    }))
    password2 = forms.CharField( widget=forms.PasswordInput(attrs= {
        "class" : "w-11/12 p-4 rounded-lg",
        "placeholder": "Please re-enter password",
        
    }))
        