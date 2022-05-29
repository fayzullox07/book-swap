from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import *

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['first_name','last_name','username','email','age','gender','year']
        widgets = {
            "username":forms.TextInput(
                attrs={
                    "class":"unique",
                    "placeholder":"Username",
                    "max_length":25
                }
            ),
            "first_name":forms.TextInput(
                attrs={
                    "class":"unique",
                    "placeholder":"First Name",
                    "max_length":25
                }
            ),
            "last_name":forms.TextInput(
                attrs={
                    "class":"unique",
                    "placeholder":"Last Name",
                    "max_length":25
                }
            ),
            "email":forms.TextInput(
                attrs={
                    "class":"unique",
                    "placeholder":"Email",
                    "max_length":25
                }
            ),
            "age":forms.TextInput(
                attrs={
                    "class":"unique",
                    "placeholder":"Your age",
                }
            ),
            "gender":forms.TextInput(
                attrs={
                    "class":"unique",
                    "placeholder":"Your gender",
                    "max_length":25
                }
            ),
            "year":forms.TextInput(
                attrs={
                    "class":"unique",
                    "placeholder":"Your year",
                }
            ),
        }   

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name','username','age','email',)
