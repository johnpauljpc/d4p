from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def home(request):
    return render(request, 'home.html')

class AboutUs(TemplateView):
    template_name = 'about.html'


class ContactUs(TemplateView):
    template_name = 'contact-us.html'