from django.test import TestCase, Client
import fund.models
import fund.forms
import fund.views
from django.contrib.auth.models import User
import random

# Create your tests here.

#Testing Models

#Test suite for ApplicationData Model
class ApplicationDataTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        fund.models.ApplicationData.objects.create(user=User.objects.create(username='User'+str(random.randint(10000,200000)),password='AbD12Cefl02'),
                            organisationName='ABC', projectTitle='BCD', CH_OSCR_number='093890', projectDesc='ABC',
                           userGroupDesc='GGJJLL', learningOpp='NOEPLRRS', keyPartnersWork='AFGCLG', projImpactClimate='KKKK',
                           projSupportLocBus='uiopla', proContribution='dsadad')

    def test_str_method(self):
        test_app = fund.models.ApplicationData.objects.get(id=1)
        expected_str = str(test_app.projectTitle)
        self.assertEqual(str(test_app), expected_str)

    def test_organisationName_label(self):
        test_app = fund.models.ApplicationData.objects.get(id=1)
        field_label = test_app._meta.get_field('organisationName').verbose_name
        self.assertEqual(field_label, 'organisationName')

    def test_organisationName_max_length(self):
        test_app = fund.models.ApplicationData.objects.get(id=1)
        max_length = test_app._meta.get_field('organisationName').max_length
        self.assertEqual(max_length, 200)

    def test_projectTitle_label(self):
        test_app = fund.models.ApplicationData.objects.get(id=1)
        field_label = test_app._meta.get_field('projectTitle').verbose_name
        self.assertEqual(field_label, 'projectTitle')

    def test_projectTitle_max_length(self):
        test_app = fund.models.ApplicationData.objects.get(id=1)
        max_length = test_app._meta.get_field('projectTitle').max_length
        self.assertEqual(max_length, 200)
        
    def test_CH_OSCR_number_label(self):
        test_app = fund.models.ApplicationData.objects.get(id=1)
        field_label = test_app._meta.get_field('CH_OSCR_number').verbose_name
        self.assertEqual(field_label, 'CH OSCR number')

    def test_CH_OSCR_number_max_length(self):
        test_app = fund.models.ApplicationData.objects.get(id=1)
        max_length = test_app._meta.get_field('CH_OSCR_number').max_length
        self.assertEqual(max_length, 20)

    def test_projectDesc_label(self):
        test_app = fund.models.ApplicationData.objects.get(id=1)
        field_label = test_app._meta.get_field('projectDesc').verbose_name
        self.assertEqual(field_label, 'projectDesc')

    def test_projectDesc_max_length(self):
        test_app = fund.models.ApplicationData.objects.get(id=1)
        max_length = test_app._meta.get_field('projectDesc').max_length
        self.assertEqual(max_length, 300)

    def test_userGroupDesc_label(self):
        test_app = fund.models.ApplicationData.objects.get(id=1)
        field_label = test_app._meta.get_field('userGroupDesc').verbose_name
        self.assertEqual(field_label, 'userGroupDesc')   

    def test_userGroupDesc_max_length(self):
        test_app = fund.models.ApplicationData.objects.get(id=1)
        max_length = test_app._meta.get_field('userGroupDesc').max_length
        self.assertEqual(max_length, 300)
        
    def test_learningOpp_label(self):
        test_app = fund.models.ApplicationData.objects.get(id=1)
        field_label = test_app._meta.get_field('learningOpp').verbose_name
        self.assertEqual(field_label, 'learningOpp')

    def test_learningOpp_max_length(self):
        test_app = fund.models.ApplicationData.objects.get(id=1)
        max_length = test_app._meta.get_field('learningOpp').max_length
        self.assertEqual(max_length, 300)

    def test_keyPartnersWork_label(self):
        test_app = fund.models.ApplicationData.objects.get(id=1)
        field_label = test_app._meta.get_field('keyPartnersWork').verbose_name
        self.assertEqual(field_label, 'keyPartnersWork')

    def test_keyPartnersWork_max_length(self):
        test_app = fund.models.ApplicationData.objects.get(id=1)
        max_length = test_app._meta.get_field('keyPartnersWork').max_length
        self.assertEqual(max_length, 300)

    def test_projImpactClimate_label(self):
        test_app = fund.models.ApplicationData.objects.get(id=1)
        field_label = test_app._meta.get_field('projImpactClimate').verbose_name
        self.assertEqual(field_label, 'projImpactClimate')

    def test_projImpactClimate_max_length(self):
        test_app = fund.models.ApplicationData.objects.get(id=1)
        max_length = test_app._meta.get_field('projImpactClimate').max_length
        self.assertEqual(max_length, 300)

    def test_projSupportLocBus_label(self):
        test_app = fund.models.ApplicationData.objects.get(id=1)
        field_label = test_app._meta.get_field('projSupportLocBus').verbose_name
        self.assertEqual(field_label, 'projSupportLocBus')

    def test_projSupportLocBus_max_length(self):
        test_app = fund.models.ApplicationData.objects.get(id=1)
        max_length = test_app._meta.get_field('projSupportLocBus').max_length
        self.assertEqual(max_length, 300)

    def test_proContribution_label(self):
        test_app = fund.models.ApplicationData.objects.get(id=1)
        field_label = test_app._meta.get_field('proContribution').verbose_name
        self.assertEqual(field_label, 'proContribution')

    def test_proContribution_max_length(self):
        test_app = fund.models.ApplicationData.objects.get(id=1)
        max_length = test_app._meta.get_field('proContribution').max_length
        self.assertEqual(max_length, 300)
#Testing Views

#Test suite for Index view
class IndexViewTest(TestCase):

    def test_index_view_load(self):

        response = self.client.get('http://127.0.0.1:8000/')
        self.assertEqual(response.status_code, 200)

    def test_index_template_used(self):

        response = self.client.get('http://127.0.0.1:8000/')
        self.assertTemplateUsed(response, 'fund/login.html') 


#Test suite for Welcome view

class WelcomeViewTest(TestCase):

    def test_welcome_view_load(self):
        
        response = self.client.get('http://127.0.0.1:8000/welcome/')
        self.assertEqual(response.status_code, 200)

    def test_welcome_template_used(self):

        #Currently displays info.html -> change to welcome.html in views
        response = self.client.get('http://127.0.0.1:8000/welcome/')
        self.assertTemplateUsed(response, 'fund/info.html')

#Test suite for info view

class InfoViewTest(TestCase):

    def test_info_view_load(self):

        response = self.client.get('http://127.0.0.1:8000/application_introduction/')
        self.assertEqual(response.status_code, 200)

    def test_info_template_used(self):

        response = self.client.get('http://127.0.0.1:8000/application_introduction/')
        self.assertTemplateUsed(response, 'fund/application_introduction.html')
            


#Test suite for base view

class BaseViewTest(TestCase):

    def test_base_view_load(self):
        
        response = self.client.get('http://127.0.0.1:8000/base/')
        self.assertEqual(response.status_code, 200)

    def test_base_template_used(self):

        response = self.client.get('http://127.0.0.1:8000/base/')
        self.assertTemplateUsed(response, 'fund/base.html')  

#Test suite for dashboard view

class DashboardViewTest(TestCase):

    def setUp(self):
        test_user1 = User.objects.create_user(username='testuser1', password='abcGGJ12Ls', email='testemail@gmail.com')
        test_user1.save()

    def test_dashboard_view_load(self):

        login = self.client.login(username='testuser1', password='abcGGJ12Ls', email='testemail@gmail.com')
        response = self.client.get('http://127.0.0.1:8000/dashboard/')
        self.assertEqual(response.status_code, 200)

    #def test_dashboard_template_used(self):

        #response = self.client.get('http://127.0.0.1:8000/dashboard/')
        #self.assertTemplateUsed(response, 'fund/dashboard.html') 

#Test suite for Register view
class RegisterViewTest(TestCase):

    def test_register_view_load(self):

        response = self.client.get('http://127.0.0.1:8000/register/')
        self.assertEqual(response.status_code, 200)

    def test_register_template_used(self):

        response = self.client.get('http://127.0.0.1:8000/register/')
        self.assertTemplateUsed(response, 'fund/register.html') 

#Test suite for Login view
class LoginViewTest(TestCase):

    
    def test_login_view_load(self):

        response = self.client.get('http://127.0.0.1:8000/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_template_used(self):

        response = self.client.get('http://127.0.0.1:8000/login/')
        self.assertTemplateUsed(response, 'fund/login.html')

#Test suite for Application view

class ApplicationViewTest(TestCase):

    
    def test_application_view_load(self):

        response = self.client.get('http://127.0.0.1:8000/application/')
        self.assertEqual(response.status_code, 200)

    def test_application_template_used(self):

        response = self.client.get('http://127.0.0.1:8000/application/')
        self.assertTemplateUsed(response, 'fund/application.html')


#Test suite for BudgetProfile view

class BudgetProfileViewTest(TestCase):
    
    def test_application_view_load(self):

        response = self.client.get('http://127.0.0.1:8000/budget_profile/')
        self.assertEqual(response.status_code, 200)

    def test_application_template_used(self):

        response = self.client.get('http://127.0.0.1:8000/budget_profile/')
        self.assertTemplateUsed(response, 'fund/budgetProfile.html')
