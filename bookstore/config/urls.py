
from django.contrib import admin
from django.urls import path, include
from allauth.account.views import SignupView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    #User management
    # path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignupView.as_view(template_name = 'registration/signup.html'), name='account_signup'),
    path('accounts/logout/', LogoutView.as_view(template_name = 'registration/logout.html'), name='account_logout'),
    path('accounts/', include('allauth.urls')),

    #Local apps
    path('accounts/', include('accounts.urls')),
    path('', include('pages.urls')),
    path('books/', include('books.urls'))
   
]
