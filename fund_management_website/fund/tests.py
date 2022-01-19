from django.test import TestCase, Client
from .models import *
from .views import *

# Create your tests here.

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

    def test_register_template_used(self):

        #Currently displays info.html -> change to welcome.html in views
        response = self.client.get('http://127.0.0.1:8000/welcome/')
        self.assertTemplateUsed(response, 'fund/info.html')


#Test suite for base view

class BaseViewTest(TestCase):

    def test_base_view_load(self):
        
        response = self.client.get('http://127.0.0.1:8000/base/')
        self.assertEqual(response.status_code, 200)

    def test_info_template_used(self):

        response = self.client.get('http://127.0.0.1:8000/base/')
        self.assertTemplateUsed(response, 'fund/base.html')  

#Test suite for dashboard view

class DashboardViewTest(TestCase):

    def test_dashboard_view_load(self):
        
        response = self.client.get('http://127.0.0.1:8000/dashboard/')
        self.assertEqual(response.status_code, 200)

    def test_info_template_used(self):

        response = self.client.get('http://127.0.0.1:8000/dashboard/')
        self.assertTemplateUsed(response, 'fund/dashboard.html') 

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
        
