from django.urls import path  
from .views import OrderBook, Charge

urlpatterns = [
    path('', OrderBook.as_view(), name="book-order"),
    path('charge/', Charge.as_view(), name="charge")
]