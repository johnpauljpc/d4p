from django.urls import path 
from .views import home, AboutUs, ContactUs


urlpatterns = [
    path('', home, name='home'),
    path('about/', AboutUs.as_view(), name="about"),
    path('contact-us/', ContactUs.as_view(), name="contact-us"),
]