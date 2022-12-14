""" Module to define different forms"""
from django import forms
from .models import UserProfile, ApplicationData, User, Comments, Review, BudgetProfile, SpendingItems


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
            'userGroupDesc' :"Co-Production (Human)",
            'learningOpp' :"Capacity building (Learning)",
            'keyPartnersWork' :"Partnership working (Systems)",
            'projImpactClimate' :"Climate and Environment",
            'projSupportLocBus' :"Local economic and resilience building",
            'proContribution' :"Social return",
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

class UpdateAppStatus(forms.ModelForm):

    class Meta:
        model = ApplicationData
        fields = ('app_status',)
        labels = {'app_status':'Change application status?'}


class FeedbackForm(forms.ModelForm):

    class Meta:

        model = ApplicationData
        fields = ('feedback',)
        labels = {'feedback': 'Comments and Feedback'}

class CommentForm(forms.ModelForm):
    """Forms for Comments"""

    class Meta:
        """Meta properties of CommentForm"""
        model = Comments
        fields = ('comment', )

        labels = { 'comment' :"Please add your comments for this application", }


class BudgetForm(forms.ModelForm):
    """Forms for Budget Allocation"""
    class Meta:
        """Meta Properties of BudgetForm"""
        model = BudgetProfile
        fields = ('totalBudget',)
        labels = {"totalBudget":"Please state total budget to be allocated to the project",}

class EvidenceForm(forms.ModelForm):
    """Form for uploading Evidence for a spending Item"""
    class Meta:
        """Meta properties of EvidenceForm"""
        model = SpendingItems
        fields = ('evidence',)
        label = {"evidence":"Please upload relevant file for this item",}




class ReviewForm(forms.ModelForm):

    class Meta:

        model = Review

        fields = ('co_production', 'capacity_building', 'partnership_working', 'climate_environment',
                  'local_economic_res_building', 'social_return_acc', 'general_feedback',
                  'review_complete',)

        labels = {

            'co_production' : 'Co-Production (Human)',
            'capacity_building' : 'Capacity building (Learning)',
            'partnership_working' : 'Partnership working (Systems)',
            'climate_environment': 'Climate and Environment',
            'local_economic_res_building' : 'Local economic and resilience building',
            'social_return_acc' : 'Social return and accountability',
            'general_feedback' : 'Comments',
            'review_complete' : 'Is the review ready to be submitted?',

        }


        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
