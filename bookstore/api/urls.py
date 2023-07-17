from django.urls import path
from .views import Home, BookRUD

urlpatterns = [
    path('', Home.as_view(), name='home' ),
    path('book/<uuid:id>/', BookRUD.as_view(), name = "book-rud"),
]