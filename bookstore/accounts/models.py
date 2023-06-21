from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(blank=False, null= False, unique=True)


    # USERNAME_FIELD = 'email' 
    # REQUIRED_FIELDS =['username']   
    
    