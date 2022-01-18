from django.test import TestCase

# Create your tests here.

#Testing Views

#Test suite for Index page
class IndexViewTest(TestCase):

    def test_index_view_load(self):

        response = self.client.get('http://127.0.0.1:8000/welcome/')
        self.assertEqual(response.status_code, 200)

#Test suite for Register page
class RegisterViewTest(TestCase):

    def test_register_view_load(self):

        response = self.client.get('http://127.0.0.1:8000/fund/register/')
        self.assertEqual(response.status_code, 200)

    def test_register_template_used(self):

        response = self.client.get('http://127.0.0.1:8000/')
        self.assertTemplateUsed(response, 'fund/register.html') 
