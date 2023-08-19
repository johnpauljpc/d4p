from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth.models import Permission
from django.conf  import settings
import stripe

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
# Create your views here.

class OrderBook(TemplateView):
    template_name = "orders/purchase.html"
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context
    
class Charge(View):
    
    def post(self, request):
        
        charge = stripe.Charge.create(
            amount = 36000,
            currency = 'usd',
            description = 'purchase all books',
            source = request.POST['stripeToken']
        )

        # Get the permission
        permission = Permission.objects.get(name = 'Can read all books')
        # or ==>  permission = Permission.objects.get(codename = "special_status")
        #get user
        u = request.user
        #add permission to user
        u.user_permissions.add(permission)
        return render(request, "orders/charge.html")