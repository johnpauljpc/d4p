from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, CreateView

# imports from local files
from .forms import CustomUserCreationForm

# Create your views here.
class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
# class SignupView(View):
#     def get(self, request):
#         form = CustomUserCreationForm()


#         return render(request, 'registration/signup.html', context={'form':form})