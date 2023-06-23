from django.test import TestCase, SimpleTestCase
from django.urls import reverse

# Create your tests here.
class TestHomePage(SimpleTestCase):
    # @classmethod
    def testHomepageStatus(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        print('url tested')

    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        print('url name tested')