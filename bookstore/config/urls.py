
from django.contrib import admin
from django.urls import path, include
import debug_toolbar


# media configuration
from django.conf.urls.static import static
from django.conf import settings

# views
from allauth.account.views import SignupView, LogoutView

urlpatterns = [
    path('debug-toolbar/', include(debug_toolbar.urls)),
    path('my-main-domain/', admin.site.urls),
    # path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),

    #User management
    # path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignupView.as_view(template_name = 'registration/signup.html'), name='account_signup'),
    path('accounts/logout/', LogoutView.as_view(template_name = 'registration/logout.html'), name='account_logout'),
    path('accounts/', include('allauth.urls')),

    #Local apps
    path('accounts/', include('accounts.urls')),
    path('', include('pages.urls')),
    path('books/', include('books.urls')),
    path('order/', include('orders.urls')),

    path('api/', include('api.urls') ),
    

   
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

