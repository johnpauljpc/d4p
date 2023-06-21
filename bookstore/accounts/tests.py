from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import CustomUser

# Create your tests here.
User = get_user_model()

class TestCustomUserModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        
        user = CustomUser.objects.create_user(
            username = 'john',
            # email = 'jp@gmail.com',
            
        )
        user.set_password('pass1234')

    def testUserCreation(self):
        user = CustomUser.objects.get(id=1)
        
        self.assertEqual(user.username, 'john')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)

    # def testCreateSuperUser(self):
    #     User.objects.create_superuser(
    #         username =
    #     )

