from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email']


class CustomUserChange(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email']