from fileinput import FileInput
from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm
from login.models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user']
        widgets = {
            'first_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'profile_image': widgets.FileInput(attrs={'class': 'form-control'}),
        }


# from typing import Any
# from django import forms
# from django.contrib.auth.forms import UserCreationForm

# class SignUpForm (UserCreationForm):
#     class Meta:
#         pass
        
    # phone_number = forms.CharField(max_length=30, required=True, help_text='Required.')
    # full_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    # username = forms.CharField(max_length=30, required=True, help_text='Required.')
    # password1 = forms.CharField(max_length=30, required=True, help_text='Required.')
    # password2 = forms.CharField(max_length=30, required=True, help_text='Required.')

    # def username(self):
    #     return self.username
    
    # def save(self):
    #     user = 
