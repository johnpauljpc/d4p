from django.urls import path  
from .views import OrderBook

urlpatterns = [
    path('', OrderBook.as_view(), name="book-order")
]