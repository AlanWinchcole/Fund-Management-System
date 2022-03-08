""" Module to define different forms"""
from django import forms
from .models import UserProfile, ApplicationData, User, Review


class UserForm(forms.ModelForm) :
    """Forms for Users"""
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        """Meta properties of UserForms"""
        model = User
        fields = ('username', 'first_name', 'last_name' ,'email', 'password')

        labels = { 'username' :"Username",
                   'first_name': 'First Name',
                   'last_name':'Last Name',
                   'email' :"Email Address",
                   'password' :'Password', }


class UserProfileForm(forms.ModelForm):
    """Extension form for Users"""
    class Meta:
        """Meta properties of UserProfileForm"""
        model = UserProfile
        fields = ("contact_number",)


class ApplicationForm(forms.ModelForm):
    """Form for Applications"""
    class Meta:
        """Meta properties for Application"""
        model = ApplicationData
        fields = ('organisationName','projectTitle' ,'CH_OSCR_number','projectDesc','userGroupDesc','learningOpp' ,'keyPartnersWork' ,'projImpactClimate' ,'projSupportLocBus',
                  'proContribution', 'application_complete')
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
            'application_complete':"Is your application complete?",

        }
        widgets = {

            'organisationName' :forms.TextInput(attrs={ 'class' :'form-control' }),
            'projectTitle' :forms.TextInput(attrs={ 'class' :'form-control' }),
            'CH_OSCR_number' :forms.TextInput(attrs={ 'class' :'form-control' }),
            # 'contactName' :forms.TextInput(attrs={ 'class' :'form-control' }),
            # 'contactEmail' :forms.TextInput(attrs={ 'class' :'form-control' }),
            'projectDesc' :forms.Textarea(attrs={ 'class' :'form-control' }),
            'userGroupDesc' :forms.Textarea(attrs={ 'class' :'form-control' }),
            'learningOpp' :forms.Textarea(attrs={ 'class' :'form-control' }),
            'keyPartnersWork' :forms.Textarea(attrs={ 'class' :'form-control' }),
            'projImpactClimate' :forms.Textarea(attrs={ 'class' :'form-control' }),
            'projSupportLocBus' :forms.Textarea(attrs={ 'class' :'form-control' }),
            'proContribution' :forms.Textarea(attrs={ 'class' :'form-control' }),
            'application_complete':forms.CheckboxInput(attrs={'class':'boolean'}),
        }


class ReviewForm(forms.ModelForm):

    class Meta:

        model = Review
        fields = ('co_production','co_production_feedback')

        labels = {

            'co_production' : 'co_production',
            'co_production_feedback' : 'co_production_feedback'

        }
