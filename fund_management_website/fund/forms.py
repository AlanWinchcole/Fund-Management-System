from django import forms
from django.forms import fields
from django.forms.models import *
#from django.forms import Modelform
from .models import *


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

        labels = {'username': "Username",
                    'email': "Email Address",
                    'password': 'Password', }



class Form(forms.ModelForm):
    userType = forms.ChoiceField()
    class Meta:
        model=UserProfile
        fields=('verified',)

        labels = {
            'verified': "Is the user verified",
            'userType': "Type of user"
        }
        widgets = {
            'userType': forms.RadioSelect(choices = [(1, "LAG Member"), (2,"Volunteer"), (3, "Applicant"), (4, "Other")])
        }

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = ApplicationData
        fields = ('__all__')
