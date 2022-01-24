from django import forms
from django.forms import fields
from django.forms.models import *
# from django.forms import Modelform
from .models import *


class UserForm(forms.ModelForm) :
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta :
        model = User
        fields = ('username', 'first_name', 'last_name' ,'email', 'password')

        labels = { 'username' :"Username",
                   'first_name': 'First Name',
                   'last_name':'Last Name',
                   'email' :"Email Address",
                   'password' :'Password', }


# class Form(forms.ModelForm) :
#     userType = forms.ChoiceField()
#
#     class Meta :
#         model = UserProfile
#         fields = ('verified',)
#
#         labels = {
#             'verified' :"Is the user verified",
#             'userType' :"Type of user"
#         }
#         widgets = {
#             'userType' :forms.RadioSelect(choices=[(1, "LAG Member"), (2, "Volunteer"), (3, "Applicant"), (4, "Other")])
#         }


class ApplicationForm(forms.ModelForm) :
    class Meta :
        model = ApplicationData
        fields = ('organisationName','projectTitle' ,'CH_OSCR_number','projectDesc','userGroupDesc','learningOpp' ,'keyPartnersWork' ,'projImpactClimate' ,'projSupportLocBus',
                  'proContribution',)
        labels = {

            'organisationName' :'Name of the Organisation',
            'projectTitle' :'Project Title',
            'CH_OSCR_number' :'OSCR Number',
            # 'contactName' :"Contact Name",
            # 'contactEmail' :"Contact Email",
            'projectDesc' :"Project Description",
            'userGroupDesc' :"User Group Description",
            'learningOpp' :"Learning Opportunity",
            'keyPartnersWork' :"Key Partners Work",
            'projImpactClimate' :"Project's Impact on Climate",
            'projSupportLocBus' :"How does project support local business?",
            'proContribution' :"Pro Contribution",

        }
        widgets = {

            'organisationName' :forms.TextInput(attrs={ 'class' :'form-control' }),
            'projectTitle' :forms.TextInput(attrs={ 'class' :'form-control' }),
            'CH_OSCR_number' :forms.TextInput(attrs={ 'class' :'form-control' }),
            # 'contactName' :forms.TextInput(attrs={ 'class' :'form-control' }),
            # 'contactEmail' :forms.TextInput(attrs={ 'class' :'form-control' }),
            'projectDesc' :forms.TextInput(attrs={ 'class' :'form-control' }),
            'userGroupDesc' :forms.TextInput(attrs={ 'class' :'form-control' }),
            'learningOpp' :forms.TextInput(attrs={ 'class' :'form-control' }),
            'keyPartnersWork' :forms.TextInput(attrs={ 'class' :'form-control' }),
            'projImpactClimate' :forms.TextInput(attrs={ 'class' :'form-control' }),
            'projSupportLocBus' :forms.TextInput(attrs={ 'class' :'form-control' }),
            'proContribution' :forms.TextInput(attrs={ 'class' :'form-control' }),


        }
