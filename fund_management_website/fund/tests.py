"""Test Module"""
import random
from django.test import TestCase
from django.contrib.auth.models import User
import fund.models
import fund.forms
import fund.views
from datetime import date


# Create your tests here.

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

        laguser = User.objects.create_superuser(username='testlag', password='12345')
        staffuser = User.objects.create_superuser(username='teststaff', password='12345')


    # as normal user
    def test_dashboard_view_load_user(self) :
        """Method the status code for dasboard"""
        self.client.login(username='testuser1', password='abcGGJ12Ls', email='testemail@gmail.com')
        response = self.client.get('http://127.0.0.1:8000/dashboard/')
        self.assertEqual(response.status_code, 200)

    # as lag user
    def test_dashboard_view_load_lag(self) :
        """Method the status code for dasboard"""
        self.client.login(username='testlag', password='12345')
        response = self.client.get('http://127.0.0.1:8000/dashboard/')
        self.assertEqual(response.status_code, 200)

    # as staff user
    def test_dashboard_view_load_staff(self) :
        """Method the status code for dasboard"""
        self.client.login(username='teststaff', password='12345')
        response = self.client.get('http://127.0.0.1:8000/dashboard/')
        self.assertEqual(response.status_code, 200)

    def test_dashboard_template_used(self):

        login = self.client.login(username='testuser1', password='abcGGJ12Ls')
        response = self.client.get('http://127.0.0.1:8000/dashboard/')
        self.assertTemplateUsed(response, 'fund/dashboard.html')


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

class ViewApplicationViewTest(TestCase):

        @classmethod
        def setUpTestData(cls) :
            """Method to define the setup data"""
            fund.models.ApplicationData.objects.create(
                user=User.objects.create(username='User' + str(random.randint(10000, 200000)), password='AbD12Cefl02'),
                organisationName='ABCD', projectTitle='BCDA', CH_OSCR_number='0938904', projectDesc='AdC',
                userGroupDesc='GGJJLL', learningOpp='NOEPLRRS', keyPartnersWork='AFGCLG', projImpactClimate='KKKK',
                projSupportLocBus='uiopla', proContribution='dsadad')

            laguser = User.objects.create_superuser(username='testlag', password='12345')
            staffuser = User.objects.create_superuser(username='teststaff', password='12345')
            normaluser = User.objects.create(username='user1234', password='12345')

        def test_view_app_status_normal_view_load(self):

            login = self.client.login(username='normaluser', password='12345')
            response = self.client.get('http://127.0.0.1:8000/view_application_status/1')
            self.assertEqual(response.status_code, 200)

        def test_view_app_status_lag_view_load(self):

            login = self.client.login(username='testlag', password='12345')
            response = self.client.get('http://127.0.0.1:8000/view_application_status/1')
            self.assertEqual(response.status_code, 200)

        def test_view_app_status_staff_view_load(self):

            login = self.client.login(username='testsatff', password='12345')
            response = self.client.get('http://127.0.0.1:8000/view_application_status/1')
            self.assertEqual(response.status_code, 200)

        def test_view_app_status_template_used(self):

            response = self.client.get('http://127.0.0.1:8000/view_application_status/1')
            self.assertTemplateUsed(response, 'fund/application_view.html')

class ViewUpdateApplicationView(TestCase):

        @classmethod
        def setUpTestData(cls) :
            """Method to define the setup data"""
            fund.models.ApplicationData.objects.create(
                user=User.objects.create(username='User', password='AbD12Cefl02'),
                organisationName='ABCD', projectTitle='BCDA', CH_OSCR_number='0938904', projectDesc='AdC',
                userGroupDesc='GGJJLL', learningOpp='NOEPLRRS', keyPartnersWork='AFGCLG', projImpactClimate='KKKK',
                projSupportLocBus='uiopla', proContribution='dsadad')

        def test_update_applcation_view_load(self):

            login = self.client.login(username='User', password='AbD12Cefl02')
            response = self.client.get('http://127.0.0.1:8000/update_application/1')
            self.assertEqual(response.status_code, 200)


        def test_update_application_template_used(self):

            response = self.client.get('http://127.0.0.1:8000/update_application/1')
            self.assertTemplateUsed(response, 'fund/application.html')








# Test suite for BudgetProfile view

class BudgetProfileViewTest(TestCase) :
    """Class to define tests for budget profile"""

    @classmethod
    def setUpTestData(cls) :

        """Method to define the setup data"""
        fund.models.ApplicationData.objects.create(
            user=User.objects.create(username='User', password='AbD12Cefl02'),
            organisationName='ABCD', projectTitle='BCDA', CH_OSCR_number='0938904', projectDesc='AdC',
            userGroupDesc='GGJJLL', learningOpp='NOEPLRRS', keyPartnersWork='AFGCLG', projImpactClimate='KKKK',
            projSupportLocBus='uiopla', proContribution='dsadad')

    def test_budget_profile_view_load(self) :
        """Method to test status code for budget profile view"""
        response = self.client.get('http://127.0.0.1:8000/budget_profile/1')
        self.assertEqual(response.status_code, 200)

    def test_budget_profile_template_used(self) :
        """Method to test if budget page is rendered correctly"""
        response = self.client.get('http://127.0.0.1:8000/budget_profile/1')
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
        """Method to test status code for review application view"""
        self.user = User.objects.create_superuser(username='testlag', password='12345')
        login = self.client.login(username='testlag', password='12345')
        response = self.client.get('http://127.0.0.1:8000/review/1')
        self.assertEqual(response.status_code, 200)

    def test_review_application_template_used(self) :
        """Method to test if review page is rendered correctly"""
        self.user = User.objects.create_superuser(username='testlag', password='12345')
        login = self.client.login(username='testlag', password='12345')
        response = self.client.get('http://127.0.0.1:8000/review/1')
        self.assertTemplateUsed(response, 'fund/review.html')

class ViewReviewTest(TestCase):

    @classmethod
    def setUpTestData(cls) :
        """Method to define the setup data"""
        fund.models.ApplicationData.objects.create(
            user=User.objects.create(username='User' + str(random.randint(10000, 200000)), password='AbD12Cefl02'),
            organisationName='ABCD', projectTitle='BCDA', CH_OSCR_number='0938904', projectDesc='AdC',
            userGroupDesc='GGJJLL', learningOpp='NOEPLRRS', keyPartnersWork='AFGCLG', projImpactClimate='KKKK',
            projSupportLocBus='uiopla', proContribution='dsadad')

        laguser = User.objects.create_superuser(username='testlag', password='12345')
        staffuser = User.objects.create_superuser(username='teststaff', password='12345')
        normaluser = User.objects.create(username='user1234', password='12345')
        fund.models.Review.objects.create(application=fund.models.ApplicationData.objects.get(id=1), user=laguser, co_production=2, capacity_building=2, partnership_working=1,
                                            climate_environment=2, local_economic_res_building=0, social_return_acc=2, general_feedback='Excellent', review_complete=True)



    #Test as LAG member
    def test_view_review_view_load(self):

        login = self.client.login(username='testlag', password='12345')
        response = self.client.get('http://127.0.0.1:8000/view_review/1')
        self.assertEqual(response.status_code, 200)

    #Test as Satff Member
    def test_view_review_view_staff_load(self):

        login = self.client.login(username='teststaff', password='12345')
        response = self.client.get('http://127.0.0.1:8000/view_review/1')
        self.assertEqual(response.status_code, 200)

    def test_view_review_template_used(self):

        login = self.client.login(username='teststaff', password='12345')
        response = self.client.get('http://127.0.0.1:8000/view_review/1')
        self.assertTemplateUsed(response, 'fund/review_view.html')

class UpdateReviewView(TestCase):

        @classmethod
        def setUpTestData(cls) :
            """Method to define the setup data"""
            fund.models.ApplicationData.objects.create(
                user=User.objects.create(username='User' + str(random.randint(10000, 200000)), password='AbD12Cefl02'),
                organisationName='ABCD', projectTitle='BCDA', CH_OSCR_number='0938904', projectDesc='AdC',
                userGroupDesc='GGJJLL', learningOpp='NOEPLRRS', keyPartnersWork='AFGCLG', projImpactClimate='KKKK',
                projSupportLocBus='uiopla', proContribution='dsadad')

            laguser = User.objects.create_superuser(username='testlag', password='12345')
            staffuser = User.objects.create_superuser(username='teststaff', password='12345')
            normaluser = User.objects.create(username='user1234', password='12345')
            fund.models.Review.objects.create(application=fund.models.ApplicationData.objects.get(id=1), user=laguser, co_production=2, capacity_building=2, partnership_working=1,
                                                climate_environment=2, local_economic_res_building=0, social_return_acc=2, general_feedback='Excellent', review_complete=True)

        def test_update_review_load(self):

            login = self.client.login(username='testlag', password='12345')
            response = self.client.get('http://127.0.0.1:8000/update_review/1')
            self.assertEqual(response.status_code, 200)

        def test_update_revivew_template_used(self):

            login = self.client.login(username='testlag', password='12345')
            response = self.client.get('http://127.0.0.1:8000/update_review/1')
            self.assertTemplateUsed(response, 'fund/review.html')


# Testing Models

# Test suite for ApplicationData Model
class ApplicationDataTest(TestCase) :
    """Tests application data"""

    @classmethod
    def setUpTestData(cls) :
        """Method to define the setup data"""
        test_app =fund.models.ApplicationData.objects.create(
            user=User.objects.create(username='User' + str(random.randint(10000, 200000)), password='AbD12Cefl02'),
            organisationName='ABC', projectTitle='BCD', CH_OSCR_number='093890', projectDesc='ABC',
            userGroupDesc='GGJJLL', learningOpp='NOEPLRRS', keyPartnersWork='AFGCLG', projImpactClimate='KKKK',
            projSupportLocBus='uiopla', proContribution='dsadad', feedback='Very good process')


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

    def test_organisationName_null(self) :
        """Method to test the null field of organisation name"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        null = test_app._meta.get_field('organisationName').null
        self.assertEqual(null, True)

    def test_organisationName_blank(self) :
        """Method to test the blank field of organisation name"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        blank = test_app._meta.get_field('organisationName').blank
        self.assertEqual(blank, True)

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

    def test_projectTitle_null(self) :
        """Method to test the null field of projectTitle"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        null = test_app._meta.get_field('projectTitle').null
        self.assertEqual(null, True)

    def test_projectTitle_blank(self) :
        """Method to test the blank field of projectTitle"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        blank = test_app._meta.get_field('projectTitle').blank
        self.assertEqual(blank, True)

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

    def test_CH_OSCR_number_null(self) :
        """Method to test the null field of CH_OSCR_number"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        null = test_app._meta.get_field('CH_OSCR_number').null
        self.assertEqual(null, True)

    def test_CH_OSCR_number_blank(self) :
        """Method to test the blank field of CH_OSCR_number"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        blank = test_app._meta.get_field('CH_OSCR_number').blank
        self.assertEqual(blank, True)

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

    def test_projectDesc_null(self) :
        """Method to test the null field of projectDesc"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        null = test_app._meta.get_field('projectDesc').null
        self.assertEqual(null, True)

    def test_projectDesc_blank(self) :
        """Method to test the blank field of projectDesc"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        blank = test_app._meta.get_field('projectDesc').blank
        self.assertEqual(blank, True)

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

    def test_userGroupDesc_null(self) :
        """Method to test the null field of userGroupDesc"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        null = test_app._meta.get_field('userGroupDesc').null
        self.assertEqual(null, True)

    def test_userGroupDesc_blank(self) :
        """Method to test the blank field of userGroupDesc"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        blank = test_app._meta.get_field('userGroupDesc').blank
        self.assertEqual(blank, True)

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

    def test_learningOpp_null(self) :
        """Method to test the null field of learningOpp"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        null = test_app._meta.get_field('learningOpp').null
        self.assertEqual(null, True)

    def test_learningOpp_blank(self) :
        """Method to test the blank field of learningOpp"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        blank = test_app._meta.get_field('learningOpp').blank
        self.assertEqual(blank, True)

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

    def test_keyPartnersWork_null(self) :
        """Method to test the null field of keyPartnersWork"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        null = test_app._meta.get_field('keyPartnersWork').null
        self.assertEqual(null, True)

    def test_keyPartnersWork_blank(self) :
        """Method to test the blank field of keyPartnersWork"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        blank = test_app._meta.get_field('keyPartnersWork').blank
        self.assertEqual(blank, True)

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

    def test_projImpactClimate_null(self) :
        """Method to test the null field of projImpactClimate"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        null = test_app._meta.get_field('projImpactClimate').null
        self.assertEqual(null, True)

    def test_projImpactClimate_blank(self) :
        """Method to test the blank field of projImpactClimate"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        blank = test_app._meta.get_field('projImpactClimate').blank
        self.assertEqual(blank, True)

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

    def test_projSupportLocBus_null(self) :
        """Method to test the null field of projSupportLocBus"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        null = test_app._meta.get_field('projSupportLocBus').null
        self.assertEqual(null, True)

    def test_projSupportLocBus_blank(self) :
        """Method to test the blank field of projSupportLocBus"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        blank = test_app._meta.get_field('projSupportLocBus').blank
        self.assertEqual(blank, True)

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

    def test_proContribution_null(self) :
        """Method to test the null field of proContribution"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        null = test_app._meta.get_field('proContribution').null
        self.assertEqual(null, True)

    def test_proContribution_blank(self) :
        """Method to test the blank field of proContribution"""
        test_app = fund.models.ApplicationData.objects.get(id=1)
        blank = test_app._meta.get_field('proContribution').blank
        self.assertEqual(blank, True)

    def test_feedback_label(self):

        test_app = fund.models.ApplicationData.objects.get(id=1)
        field_label = test_app._meta.get_field('feedback').verbose_name
        self.assertEqual(field_label, 'feedback')

    def test_feedback_max_length(self):

        test_app = fund.models.ApplicationData.objects.get(id=1)
        max_length = test_app._meta.get_field('feedback').max_length
        self.assertEqual(max_length, 200)

    def test_feedback_null(self):

        test_app = fund.models.ApplicationData.objects.get(id=1)
        null = test_app._meta.get_field('feedback').null
        self.assertTrue(null, True)

    def test_feedback_blank(self):

        test_app = fund.models.ApplicationData.objects.get(id=1)
        blank = test_app._meta.get_field('feedback').blank
        self.assertTrue(blank, True)

    def test_app_status_label(self):

        test_app = fund.models.ApplicationData.objects.get(id=1)
        field_label = test_app._meta.get_field('app_status').verbose_name
        self.assertEqual(field_label, 'app status')

    def test_app_status_default(self):

        test_app = fund.models.ApplicationData.objects.get(id=1)
        app_satus = test_app._meta.get_field('app_status').default
        self.assertEqual(app_satus, 'Pending')

    def test_reviewed_label(self):

        test_app = fund.models.ApplicationData.objects.get(id=1)
        reviewed = test_app._meta.get_field('reviewed').verbose_name
        self.assertEqual(reviewed, 'reviewed')

    def test_reviewed_default_false(self):

        test_app = fund.models.ApplicationData.objects.get(id=1)
        reviewed = test_app._meta.get_field('reviewed').default
        self.assertFalse(reviewed)

    def test_date_of_application_label(self):

        test_app = fund.models.ApplicationData.objects.get(id=1)
        field = test_app._meta.get_field('date_of_application').verbose_name
        self.assertEqual(field, 'date of application')

    def test_organisationName_value(self):

        test_app = fund.models.ApplicationData.objects.get(id=1)
        orgname = test_app.organisationName
        self.assertEqual(orgname, 'ABC')

    def test_projectTitle_value(self):

        test_app = fund.models.ApplicationData.objects.get(id=1)
        title = test_app.projectTitle
        self.assertEqual(title, 'BCD')

    def test_CH_OSCR_number_value(self):

        test_app = fund.models.ApplicationData.objects.get(id=1)
        number = test_app.CH_OSCR_number
        self.assertEqual(number, '093890')

    def test_projectDesc_value(self):

        test_app = fund.models.ApplicationData.objects.get(id=1)
        projectd = test_app.projectDesc
        self.assertEqual(projectd, 'ABC')

    def test_userGroupDesc_value(self):

        test_app = fund.models.ApplicationData.objects.get(id=1)
        usergroup = test_app.userGroupDesc
        self.assertEqual(usergroup, 'GGJJLL')

    def test_learningOpp_value(self):

        test_app = fund.models.ApplicationData.objects.get(id=1)
        learn = test_app.learningOpp
        self.assertEqual(learn, 'NOEPLRRS')

    def test_keyPartnersWork_value(self):

        test_app = fund.models.ApplicationData.objects.get(id=1)
        partners = test_app.keyPartnersWork
        self.assertEqual(partners, 'AFGCLG')

    def test_projImpactClimate_value(self):

        test_app = fund.models.ApplicationData.objects.get(id=1)
        climate = test_app.projImpactClimate
        self.assertEqual(climate, 'KKKK')

    def test_projSupportLocBus_value(self):

        test_app = fund.models.ApplicationData.objects.get(id=1)
        loc = test_app.projSupportLocBus
        self.assertEqual(loc, 'uiopla')

    def test_proContribution_value(self):

        test_app = fund.models.ApplicationData.objects.get(id=1)
        contrib = test_app.proContribution
        self.assertEqual(contrib, 'dsadad')

    def test_feedback_value(self):

        test_app = fund.models.ApplicationData.objects.get(id=1)
        fb = test_app.feedback
        self.assertEqual(fb, 'Very good process')


# Test suite for Review Model
class ReviewTest(TestCase):

        @classmethod
        def setUpTestData(cls) :
            """Method to define the setup data"""
            fund.models.ApplicationData.objects.create(
                user=User.objects.create(username='User' + str(random.randint(10000, 200000)), password='AbD12Cefl02'),
                organisationName='ABCD', projectTitle='BCDA', CH_OSCR_number='0938904', projectDesc='AdC',
                userGroupDesc='GGJJLL', learningOpp='NOEPLRRS', keyPartnersWork='AFGCLG', projImpactClimate='KKKK',
                projSupportLocBus='uiopla', proContribution='dsadad')

            laguser = User.objects.create_superuser(username='testlag', password='12345')
            staffuser = User.objects.create_superuser(username='teststaff', password='12345')
            normaluser = User.objects.create(username='user1234', password='12345')
            fund.models.Review.objects.create(application=fund.models.ApplicationData.objects.get(id=1), user=laguser, co_production=2, capacity_building=2, partnership_working=1,
                                                climate_environment=2, local_economic_res_building=0, social_return_acc=2, general_feedback='Excellent', review_complete=True)


        def test_co_prodcution_label(self):

            test_rev= fund.models.Review.objects.get(id=1)
            field_label = test_rev._meta.get_field('co_production').verbose_name
            self.assertEqual(field_label, 'co production')

        def test_co_production_default(self):

            test_rev = fund.models.Review.objects.get(id=1)
            co_pro = test_rev._meta.get_field('co_production').default
            self.assertEqual(co_pro, 0)

        def test_co_production_value(self):

            test_rev = fund.models.Review.objects.get(id=1)
            co_pro = test_rev.co_production
            self.assertEqual(co_pro, 2)

        def test_capacity_building_label(self):

            test_rev = fund.models.Review.objects.get(id=1)
            field_label = test_rev._meta.get_field('capacity_building').verbose_name
            self.assertEqual(field_label, 'capacity building')

        def test_capacity_building_default(self):

            test_rev = fund.models.Review.objects.get(id=1)
            cap = test_rev._meta.get_field('capacity_building').default
            self.assertEqual(cap, 0)

        def test_capacity_building_value(self):

            test_rev = fund.models.Review.objects.get(id=1)
            cap = test_rev.capacity_building
            self.assertEqual(cap, 2)

        def test_partnership_working_label(self):

            test_rev = fund.models.Review.objects.get(id=1)
            field_label = test_rev._meta.get_field('partnership_working').verbose_name
            self.assertEqual(field_label, 'partnership working')

        def test_partnership_working_default(self):

            test_rev = fund.models.Review.objects.get(id=1)
            pw = test_rev._meta.get_field('partnership_working').default
            self.assertEqual(pw, 0)

        def test_partnership_working_value(self):

            test_rev = fund.models.Review.objects.get(id=1)
            pw = test_rev.partnership_working
            self.assertEqual(pw, 1)

        def test_climate_environment_label(self):

            test_rev = fund.models.Review.objects.get(id=1)
            field_label = test_rev._meta.get_field('climate_environment').verbose_name
            self.assertEqual(field_label, 'climate environment')

        def test_climate_environment_default(self):

            test_rev = fund.models.Review.objects.get(id=1)
            ce = test_rev._meta.get_field('climate_environment').default
            self.assertEqual(ce, 0)

        def test_climate_environment_value(self):

            test_rev = fund.models.Review.objects.get(id=1)
            ce = test_rev.climate_environment
            self.assertEqual(ce, 2)

        def test_local_economic_res_building_label(self):

            test_rev = fund.models.Review.objects.get(id=1)
            field_label = test_rev._meta.get_field('local_economic_res_building').verbose_name
            self.assertEqual(field_label, 'local economic res building')

        def test_local_economic_res_building_default(self):

            test_rev = fund.models.Review.objects.get(id=1)
            local = test_rev._meta.get_field('local_economic_res_building').default
            self.assertEqual(local, 0)

        def test_local_economic_res_building_value(self):

            test_rev = fund.models.Review.objects.get(id=1)
            local = test_rev.local_economic_res_building
            self.assertEqual(local, 0)

        def test_social_return_acc_label(self):

            test_rev = fund.models.Review.objects.get(id=1)
            field_label = test_rev._meta.get_field('social_return_acc').verbose_name
            self.assertEqual(field_label, 'social return acc')

        def test_social_return_acc_default(self):

            test_rev = fund.models.Review.objects.get(id=1)
            social = test_rev._meta.get_field('social_return_acc').default
            self.assertEqual(social, 0)

        def test_social_return_acc_value(self):

            test_rev = fund.models.Review.objects.get(id=1)
            social = test_rev.local_economic_res_building
            self.assertEqual(social, 0)

        def test_general_feedback_label(self):

            test_rev = fund.models.Review.objects.get(id=1)
            field_label = test_rev._meta.get_field('general_feedback').verbose_name
            self.assertEqual(field_label, 'general feedback')

        def test_general_feedback_value(self):

            test_rev = fund.models.Review.objects.get(id=1)
            fb = test_rev.general_feedback
            self.assertEqual(fb, 'Excellent')


        def test_review_complete_label(self):

            test_rev = fund.models.Review.objects.get(id=1)
            field_label = test_rev._meta.get_field('review_complete').verbose_name
            self.assertEqual(field_label, 'review complete')


        def test_review_complete_value(self):

            test_rev = fund.models.Review.objects.get(id=1)
            rc = test_rev.review_complete
            self.assertTrue(rc)

class UserProfileTest(TestCase):

        @classmethod
        def setUpTestData(cls) :
            """Method to define the setup data"""
            normaluser = User.objects.create(username='user1234', password='12345')
            profile = fund.models.UserProfile.objects.create(user=normaluser, contact_number='+4499039211')

        def test_contact_label(self):

            test_profile = fund.models.UserProfile.objects.get(id=1)
            field_label = test_profile._meta.get_field('contact_number').verbose_name
            self.assertEqual(field_label, 'contact number')

        def test_contact_value(self):

            test_profile = fund.models.UserProfile.objects.get(id=1)
            number = test_profile.contact_number
            self.assertEqual(number, '+4499039211')

        def test_contact_max_len(self):

            test_profile = fund.models.UserProfile.objects.get(id=1)
            max = test_profile._meta.get_field('contact_number').max_length
            self.assertEqual(max, 12)

class ApplicationForm(TestCase):

        @classmethod
        def setUpTestData(cls) :
            """Method to define the setup data"""
            normaluser = User.objects.create(username='user1234', password='12345')
            fund.models.ApplicationData.objects.create(user=normaluser,organisationName='ABCD',
             projectTitle='BCDA', CH_OSCR_number='0938904', projectDesc='AdC',userGroupDesc='GGJJLL', learningOpp='NOEPLRRS',
              keyPartnersWork='AFGCLG', projImpactClimate='KKKK',projSupportLocBus='uiopla', proContribution='dsadad')



            laguser = User.objects.create_superuser(username='testlag', password='12345')
            staffuser = User.objects.create_superuser(username='teststaff', password='12345')

        def test_app_form_creation(self):

            form = fund.forms.ApplicationForm(data={'organisationName':'ABCD','projectTitle':'BCDA', 'CH_OSCR_number':'0938904', 'projectDesc':'AdC',
            'userGroupDesc':'GGJJLL', 'learningOpp':'NOEPLRRS', 'keyPartnersWork':'AFGCLG', 'projImpactClimate':'KKKK',
            'projSupportLocBus':'uiopla', 'proContribution':'dsadad','application_complete':True})

            self.assertTrue(isinstance(form, fund.forms.ApplicationForm))
