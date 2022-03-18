"""Test Module"""
import random
from django.test import TestCase
from django.contrib.auth.models import User
import fund.models
import fund.forms
import fund.views



# Create your tests here.

# Testing Models

# Test suite for ApplicationData Model
class ApplicationDataTest(TestCase) :
    """Tests application data"""

    @classmethod
    def setUpTestData(cls) :
        """Method to define the setup data"""
        fund.models.ApplicationData.objects.create(
            user=User.objects.create(username='User' + str(random.randint(10000, 200000)), password='AbD12Cefl02'),
            organisationName='ABC', projectTitle='BCD', CH_OSCR_number='093890', projectDesc='ABC',
            userGroupDesc='GGJJLL', learningOpp='NOEPLRRS', keyPartnersWork='AFGCLG', projImpactClimate='KKKK',
            projSupportLocBus='uiopla', proContribution='dsadad')

    def test_str_method(self) :
        """Method to test the if application was created properly"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        expected_str = str(test_app.id)
        self.assertEqual(str(test_app), expected_str)

    def test_organisationName_label(self) :
        """Method to test organisation name"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        field_label = test_app._meta.get_field('organisationName').verbose_name
        self.assertEqual(field_label, 'organisationName')

    def test_organisationName_max_length(self) :
        """Method to test the maximum length of organisation name"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        max_length = test_app._meta.get_field('organisationName').max_length
        self.assertEqual(max_length, 200)

    def test_projectTitle_label(self) :
        """ Method to test project title"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        field_label = test_app._meta.get_field('projectTitle').verbose_name
        self.assertEqual(field_label, 'projectTitle')

    def test_projectTitle_max_length(self) :
        """Method to test project title max length"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        max_length = test_app._meta.get_field('projectTitle').max_length
        self.assertEqual(max_length, 200)

    def test_CH_OSCR_number_label(self) :
        """Method to test Ch_OSCR number"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        field_label = test_app._meta.get_field('CH_OSCR_number').verbose_name
        self.assertEqual(field_label, 'CH OSCR number')

    def test_CH_OSCR_number_max_length(self) :
        """Method to test maximum length of OSCR number"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        max_length = test_app._meta.get_field('CH_OSCR_number').max_length
        self.assertEqual(max_length, 20)

    def test_projectDesc_label(self) :
        """Method to test the project description"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        field_label = test_app._meta.get_field('projectDesc').verbose_name
        self.assertEqual(field_label, 'projectDesc')

    def test_projectDesc_max_length(self) :
        """Method to test maximum length of project description"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        max_length = test_app._meta.get_field('projectDesc').max_length
        self.assertEqual(max_length, 300)

    def test_userGroupDesc_label(self) :
        """Method to test user group description label"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        field_label = test_app._meta.get_field('userGroupDesc').verbose_name
        self.assertEqual(field_label, 'userGroupDesc')

    def test_userGroupDesc_max_length(self) :
        """Method to test max length of user group description"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        max_length = test_app._meta.get_field('userGroupDesc').max_length
        self.assertEqual(max_length, 300)

    def test_learningOpp_label(self) :
        """Method to test learning opportunity field"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        field_label = test_app._meta.get_field('learningOpp').verbose_name
        self.assertEqual(field_label, 'learningOpp')

    def test_learningOpp_max_length(self) :
        """Method to test max length of learning opportunity field"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        max_length = test_app._meta.get_field('learningOpp').max_length
        self.assertEqual(max_length, 300)

    def test_keyPartnersWork_label(self) :
        """Method to test Key partners work field"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        field_label = test_app._meta.get_field('keyPartnersWork').verbose_name
        self.assertEqual(field_label, 'keyPartnersWork')

    def test_keyPartnersWork_max_length(self) :
        """Method to test max length of Key partners work field"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        max_length = test_app._meta.get_field('keyPartnersWork').max_length
        self.assertEqual(max_length, 300)

    def test_projImpactClimate_label(self) :
        """Method to test Impact Climate field"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        field_label = test_app._meta.get_field('projImpactClimate').verbose_name
        self.assertEqual(field_label, 'projImpactClimate')

    def test_projImpactClimate_max_length(self) :
        """Method to test max length of Impact Climate field"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        max_length = test_app._meta.get_field('projImpactClimate').max_length
        self.assertEqual(max_length, 300)

    def test_projSupportLocBus_label(self) :
        """Method to test Support Local Business  field"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        field_label = test_app._meta.get_field('projSupportLocBus').verbose_name
        self.assertEqual(field_label, 'projSupportLocBus')

    def test_projSupportLocBus_max_length(self) :
        """Method to test max length of Support Local Business  field"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        max_length = test_app._meta.get_field('projSupportLocBus').max_length
        self.assertEqual(max_length, 300)

    def test_proContribution_label(self) :
        """Method to test Pro Contribution  field"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        field_label = test_app._meta.get_field('proContribution').verbose_name
        self.assertEqual(field_label, 'proContribution')

    def test_proContribution_max_length(self) :
        """Method to test max length of Pro Contribution  field"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        max_length = test_app._meta.get_field('proContribution').max_length
        self.assertEqual(max_length, 300)
# Testing Views

# Test suite for Index view
class IndexViewTest(TestCase) :
    """Class to define tests for Index views"""

    def test_index_view_load(self) :
        """Test the index view's status """
        response = self.client.get('http://127.0.0.1:8000/')
        self.assertEqual(response.status_code, 200)

    def test_index_template_used(self) :
        """Test index view"""
        response = self.client.get('http://127.0.0.1:8000/')
        self.assertTemplateUsed(response, 'fund/login.html')

    # Test suite for Welcome view


class WelcomeViewTest(TestCase) :
    """Class defines test for Welcome View"""

    def test_welcome_view_load(self) :
        """Method to test the status code for welcome page"""
        response = self.client.get('http://127.0.0.1:8000/welcome/')
        self.assertEqual(response.status_code, 200)

    def test_welcome_template_used(self) :
        """Method to test view returned by welcome view"""
        # Currently displays info.html -> change to welcome.html in views
        response = self.client.get('http://127.0.0.1:8000/welcome/')
        self.assertTemplateUsed(response, 'fund/info.html')


# Test suite for info view

class InfoViewTest(TestCase) :
    """Class to define tests for info views."""

    def test_info_view_load(self) :
        """Method to test status code for info view"""
        response = self.client.get('http://127.0.0.1:8000/application_introduction/')
        self.assertEqual(response.status_code, 200)

    def test_info_template_used(self) :
        """Method to test view returned by info view."""
        response = self.client.get('http://127.0.0.1:8000/application_introduction/')
        self.assertTemplateUsed(response, 'fund/application_introduction.html')


# Test suite for base view

class BaseViewTest(TestCase) :
    """Class to define test for base view"""

    def test_base_view_load(self) :
        """Method to test status code for base view"""
        response = self.client.get('http://127.0.0.1:8000/base/')
        self.assertEqual(response.status_code, 200)

    def test_base_template_used(self) :
        """Method to test view returned by base view"""
        response = self.client.get('http://127.0.0.1:8000/base/')
        self.assertTemplateUsed(response, 'fund/base.html')

    # Test suite for dashboard view


class DashboardViewTest(TestCase) :
    """Class to define test for dashboard"""

    def setUp(self) :
        """Method to define variable require to carry out the test"""
        test_user1 = User.objects.create_user(username='testuser1', password='abcGGJ12Ls', email='testemail@gmail.com')
        test_user1_concact = fund.models.UserProfile.objects.get_or_create(user = test_user1, contact_number = 98776546)[0]
        test_user1_concact.save()
        test_user1.save()

    def test_dashboard_view_load(self) :
        """Method the status code for dasboard"""
        self.client.login(username='testuser1', password='abcGGJ12Ls', email='testemail@gmail.com')
        response = self.client.get('http://127.0.0.1:8000/dashboard/')
        self.assertEqual(response.status_code, 200)

    # def test_dashboard_template_used(self):

    # response = self.client.get('http://127.0.0.1:8000/dashboard/')
    # self.assertTemplateUsed(response, 'fund/dashboard.html')


# Test suite for Register view
class RegisterViewTest(TestCase) :
    """Class to define tests for register view"""

    def test_register_view_load(self) :
        """Method to test status code for register view"""
        response = self.client.get('http://127.0.0.1:8000/register/')
        self.assertEqual(response.status_code, 200)

    def test_register_template_used(self) :
        """Method to test if the register pages renders correctly"""
        response = self.client.get('http://127.0.0.1:8000/register/')
        self.assertTemplateUsed(response, 'fund/register.html')

    # Test suite for Login view


class LoginViewTest(TestCase) :
    """Class to define tests for login view"""

    def test_login_view_load(self) :
        """Method to test status code for login view"""
        response = self.client.get('http://127.0.0.1:8000/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_template_used(self) :
        """Method to test if the login page renders correctly"""
        response = self.client.get('http://127.0.0.1:8000/login/')
        self.assertTemplateUsed(response, 'fund/login.html')


# Test suite for Application view

class ApplicationViewTest(TestCase) :
    """Class that defines test methods for application view"""

    def test_application_view_load(self) :
        """Method to test the status code for application view"""
        response = self.client.get('http://127.0.0.1:8000/apply/')
        self.assertEqual(response.status_code, 200)

    def test_application_template_used(self) :
        """Method to see if the application view is rendered correctly"""
        response = self.client.get('http://127.0.0.1:8000/apply/')
        self.assertTemplateUsed(response, 'fund/application.html')


# Test suite for BudgetProfile view

class BudgetProfileViewTest(TestCase) :
    """Class to define tests for budget profile"""

    def test_budget_profile_view_load(self) :
        """Method to test status code for budget profile view"""
        response = self.client.get('http://127.0.0.1:8000/budget_profile/')
        self.assertEqual(response.status_code, 200)

    def test_budget_profile_template_used(self) :
        """Method to test if budget page is rendered correctly"""
        response = self.client.get('http://127.0.0.1:8000/budget_profile/')
        self.assertTemplateUsed(response, 'fund/budgetProfile.html')

# Test suite for reviewApplication views

class ReviewApplicationViewTest(TestCase):
    """Class to define tests for review page"""

    @classmethod
    def setUpTestData(cls) :
        """Method to define the setup data"""
        fund.models.ApplicationData.objects.create(
            user=User.objects.create(username='User' + str(random.randint(10000, 200000)), password='AbD12Cefl02'),
            organisationName='ABCD', projectTitle='BCDA', CH_OSCR_number='0938904', projectDesc='AdC',
            userGroupDesc='GGJJLL', learningOpp='NOEPLRRS', keyPartnersWork='AFGCLG', projImpactClimate='KKKK',
            projSupportLocBus='uiopla', proContribution='dsadad')

    def test_review_application_view_load(self) :
        """Method to test status code for budget profile view"""
        self.user = User.objects.create_superuser(username='testlag', password='12345')
        login = self.client.login(username='testlag', password='12345')
        response = self.client.get('http://127.0.0.1:8000/review/1')
        self.assertEqual(response.status_code, 200)

    def test_review_application_template_used(self) :
        """Method to test if budget page is rendered correctly"""
        response = self.client.get('http://127.0.0.1:8000/review/1')
        self.assertTemplateUsed(response, 'fund/review.html')
