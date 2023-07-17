from django.urls import path
from .views import Home, BookRUD

urlpatterns = [
    path('', Home.as_view(), name='home-api' ),
    path('book/<uuid:pk>/', BookRUD.as_view(), name = "book-rud"),
]