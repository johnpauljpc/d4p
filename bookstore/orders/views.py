from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class OrderBook(TemplateView):
    template_name = "temp_name.html"