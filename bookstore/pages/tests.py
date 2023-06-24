from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import home

# Create your tests here.
class TestHomePage(SimpleTestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)
    def testHomepageStatus(self):
        self.assertEqual(self.response.status_code, 200)
        print('url tested')

    def test_homepage_url_name(self):
        self.assertEqual(self.response.status_code, 200)
        print('url name tested')

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Halo')

    def test_resolve_home(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, home.__name__)